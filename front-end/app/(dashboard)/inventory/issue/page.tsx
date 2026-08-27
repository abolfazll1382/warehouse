import { PageHeader } from "@/components/shared/page-header";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { inventoryItems } from "@/lib/data/inventory";
import { PackageMinus } from "lucide-react";

const reasons = ["فروش به مشتری", "مصرف در خط تولید", "انتقال بین انبارها", "ضایعات / اسقاط", "مرجوعی به تامین‌کننده"];

export default function InventoryIssuePage() {
  return (
    <>
      <PageHeader title="خروج / حذف کالا" description="ثبت حواله خروج کالا و کسر از موجودی انبار" />

      <Card className="mx-auto max-w-3xl">
        <CardHeader>
          <CardTitle>اطلاعات حواله خروج کالا</CardTitle>
          <CardDescription>فیلدهای ستاره‌دار تکمیل آن‌ها الزامی است.</CardDescription>
        </CardHeader>
        <CardContent>
          <form className="grid grid-cols-1 gap-x-4 gap-y-5 md:grid-cols-2">
            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="item">
                کالا <span className="text-destructive">*</span>
              </Label>
              <Select dir="rtl">
                <SelectTrigger id="item" className="w-full">
                  <SelectValue placeholder="انتخاب کالا از انبار..." />
                </SelectTrigger>
                <SelectContent>
                  {inventoryItems.map((item) => (
                    <SelectItem key={item.id} value={item.id}>
                      {item.name} — موجودی فعلی: {item.quantity.toLocaleString("fa-IR")} {item.unit}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="quantity">
                مقدار خروجی <span className="text-destructive">*</span>
              </Label>
              <Input id="quantity" type="number" placeholder="۰" min={0} />
            </div>

            <div className="space-y-2">
              <Label htmlFor="reason">
                علت خروج <span className="text-destructive">*</span>
              </Label>
              <Select dir="rtl">
                <SelectTrigger id="reason" className="w-full">
                  <SelectValue placeholder="انتخاب علت..." />
                </SelectTrigger>
                <SelectContent>
                  {reasons.map((r) => (
                    <SelectItem key={r} value={r}>
                      {r}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="recipient">تحویل‌گیرنده / مقصد</Label>
              <Input id="recipient" placeholder="نام واحد یا مشتری" />
            </div>

            <div className="space-y-2">
              <Label htmlFor="issue-date">
                تاریخ خروج <span className="text-destructive">*</span>
              </Label>
              <Input id="issue-date" placeholder="۱۴۰۵/۰۵/۰۸" />
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="notes">توضیحات</Label>
              <Textarea id="notes" placeholder="توضیحات تکمیلی حواله خروج را وارد کنید..." rows={4} />
            </div>

            <div className="flex items-center justify-end gap-2 border-t border-border/60 pt-5 md:col-span-2">
              <Button type="button" variant="outline">
                انصراف
              </Button>
              <Button type="submit" variant="destructive">
                <PackageMinus />
                ثبت حواله خروج
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </>
  );
}
