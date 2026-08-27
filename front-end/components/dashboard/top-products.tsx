import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { formatToman } from "@/lib/utils"
import type { TopProduct } from "@/types"

export function TopProducts({ products }: { products: TopProduct[] }) {
  return (
    <Card className="h-full">
      <CardHeader>
        <CardTitle>پرفروش‌ترین محصولات</CardTitle>
        <CardDescription>سهم هر محصول از فروش ماه جاری</CardDescription>
      </CardHeader>
      <CardContent className="flex flex-col gap-5">
        {products.map((p, index) => (
          <div key={p.id} className="flex flex-col gap-1.5">
            <div className="flex items-center justify-between gap-2 text-sm">
              <span className="flex items-center gap-2 font-medium text-foreground">
                <span className="flex size-5 items-center justify-center rounded-full bg-secondary text-[11px] text-muted-foreground tabular-nums">
                  {index + 1}
                </span>
                {p.name}
              </span>
              <span className="shrink-0 text-xs text-muted-foreground tabular-nums">{p.share}٪</span>
            </div>
            <div className="h-1.5 w-full overflow-hidden rounded-full bg-secondary">
              <div
                className="h-full rounded-full bg-gradient-to-l from-primary to-chart-5"
                style={{ width: `${p.share}%` }}
              />
            </div>
            <span className="text-xs text-muted-foreground tabular-nums">{formatToman(p.amount)}</span>
          </div>
        ))}
      </CardContent>
    </Card>
  )
}
