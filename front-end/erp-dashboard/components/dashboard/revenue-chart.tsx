"use client";

import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { Card, CardAction, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { formatNumber } from "@/lib/utils";
import type { MonthlyPoint } from "@/types";

const SALES_COLOR = "var(--color-chart-1)";
const ORDERS_COLOR = "var(--color-chart-2)";

function ChartTooltip({
  active,
  payload,
  label,
}: {
  active?: boolean;
  payload?: { value: number; dataKey: string }[];
  label?: string;
}) {
  if (!active || !payload?.length) return null;

  const sales = payload.find((p) => p.dataKey === "sales")?.value ?? 0;
  const orders = payload.find((p) => p.dataKey === "orders")?.value ?? 0;

  return (
    <div className="min-w-40 rounded-lg border border-border/60 bg-popover/95 p-3 text-xs shadow-xl backdrop-blur-xl">
      <p className="mb-2 font-medium text-foreground">{label}</p>
      <div className="flex items-center justify-between gap-4 py-0.5">
        <span className="flex items-center gap-1.5 text-muted-foreground">
          <span className="size-2 rounded-full" style={{ backgroundColor: SALES_COLOR }} />
          فروش
        </span>
        <span className="font-medium tabular-nums text-foreground">
          {formatNumber(sales)} م.ت
        </span>
      </div>
      <div className="flex items-center justify-between gap-4 py-0.5">
        <span className="flex items-center gap-1.5 text-muted-foreground">
          <span className="size-2 rounded-full" style={{ backgroundColor: ORDERS_COLOR }} />
          سفارشات
        </span>
        <span className="font-medium tabular-nums text-foreground">
          {formatNumber(orders)} سفارش
        </span>
      </div>
    </div>
  );
}

export function RevenueChart({ data }: { data: MonthlyPoint[] }) {
  return (
    <Card className="h-full">
      <CardHeader>
        <CardTitle>روند فروش ماهانه</CardTitle>
        <CardDescription>مقایسه فروش (میلیون تومان) و تعداد سفارشات در ۷ ماه اخیر</CardDescription>
        <CardAction>
          <div className="flex items-center gap-3 text-xs text-muted-foreground">
            <span className="flex items-center gap-1.5">
              <span className="size-2 rounded-full" style={{ backgroundColor: SALES_COLOR }} />
              فروش
            </span>
            <span className="flex items-center gap-1.5">
              <span className="size-2 rounded-full" style={{ backgroundColor: ORDERS_COLOR }} />
              سفارشات
            </span>
          </div>
        </CardAction>
      </CardHeader>
      <CardContent className="h-[300px] ps-0 pe-4">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data} margin={{ top: 10, right: 8, bottom: 0, left: 8 }}>
            <defs>
              <linearGradient id="salesFill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor={SALES_COLOR} stopOpacity={0.35} />
                <stop offset="100%" stopColor={SALES_COLOR} stopOpacity={0} />
              </linearGradient>
              <linearGradient id="ordersFill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor={ORDERS_COLOR} stopOpacity={0.25} />
                <stop offset="100%" stopColor={ORDERS_COLOR} stopOpacity={0} />
              </linearGradient>
            </defs>
            <CartesianGrid vertical={false} stroke="var(--color-border)" strokeDasharray="4 8" />
            <XAxis
              dataKey="month"
              axisLine={false}
              tickLine={false}
              tick={{ fill: "var(--color-muted-foreground)", fontSize: 12 }}
              dy={8}
            />
            <YAxis
              axisLine={false}
              tickLine={false}
              tick={{ fill: "var(--color-muted-foreground)", fontSize: 12 }}
              tickFormatter={(v: number) => formatNumber(v)}
              width={40}
            />
            <Tooltip content={<ChartTooltip />} cursor={{ stroke: "var(--color-border)" }} />
            <Area
              type="monotone"
              dataKey="orders"
              stroke={ORDERS_COLOR}
              strokeWidth={2}
              fill="url(#ordersFill)"
            />
            <Area
              type="monotone"
              dataKey="sales"
              stroke={SALES_COLOR}
              strokeWidth={2.5}
              fill="url(#salesFill)"
            />
          </AreaChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}
