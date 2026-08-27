import { PageHeader } from "@/components/shared/page-header";
import { KpiCard } from "@/components/dashboard/kpi-card";
import { RevenueChart } from "@/components/dashboard/revenue-chart";
import { TopProducts } from "@/components/dashboard/top-products";
import { RecentTransactions } from "@/components/dashboard/recent-transactions";
import { Button } from "@/components/ui/button";
import { Download, Plus } from "lucide-react";
import { kpis, monthlyData, recentTransactions, topProducts } from "@/lib/data/dashboard";

export default function OverviewPage() {
  return (
    <>
      <PageHeader
        title="نمای کلی"
        description="خلاصه‌ای از عملکرد سازمان در ماه جاری"
        actions={
          <>
            <Button variant="outline" size="sm">
              <Download />
              دانلود گزارش
            </Button>
            <Button size="sm">
              <Plus />
              تراکنش جدید
            </Button>
          </>
        }
      />

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
        {kpis.map((kpi) => (
          <KpiCard key={kpi.id} kpi={kpi} />
        ))}
      </div>

      <div className="mt-4 grid grid-cols-1 gap-4 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <RevenueChart data={monthlyData} />
        </div>
        <TopProducts products={topProducts} />
      </div>

      <div className="mt-4">
        <RecentTransactions transactions={recentTransactions} />
      </div>
    </>
  );
}
