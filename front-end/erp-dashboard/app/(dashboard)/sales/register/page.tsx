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
import { customers } from "@/lib/data/sales";
import { topProducts } from "@/lib/data/dashboard";
import { Save } from "lucide-react";

export default function SalesRegisterPage() {
  return (
    <>
      <PageHeader title="ثبت فروش" description="ثبت فاکتور فروش جدید برای مشتریان" />

      <Card className="mx-auto max-w-3xl">
        <CardHeader>
          <CardTitle>اطلاعات فاکتور فروش</CardTitle>
          <CardDescription>فیلدهای ستاره‌دار تکمیل آن‌ها الزامی است.</CardDescription>
        </CardHeader>
        <CardContent>
          <form className="grid grid-cols-1 gap-x-4 gap-y-5 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="customer">
                مشتری <span className="text-destructive">*</span>
              </Label>
              <Select dir="rtl">
                <SelectTrigger id="customer" className="w-full">
                  <SelectValue placeholder="انتخاب مشتری..." />
                </SelectTrigger>
                <SelectContent>
                  {customers.map((c) => (
                    <SelectItem key={c.id} value={c.id}>
                      {c.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="product">
                محصول <span className="text-destructive">*</span>
              </Label>
              <Select dir="rtl">
                <SelectTrigger id="product" className="w-full">
                  <SelectValue placeholder="انتخاب محصول..." />
                </SelectTrigger>
                <SelectContent>
                  {topProducts.map((p) => (
                    <SelectItem key={p.id} value={p.id}>
                      {p.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="quantity">
                تعداد / مقدار <span className="text-destructive">*</span>
              </Label>
              <Input id="quantity" type="number" placeholder="۰" min={0} />
            </div>

            <div className="space-y-2">
              <Label htmlFor="unit-price">
                قیمت واحد (تومان) <span className="text-destructive">*</span>
              </Label>
              <Input id="unit-price" type="number" placeholder="۰" min={0} />
            </div>

            <div className="space-y-2">
              <Label htmlFor="invoice-date">
                تاریخ فاکتور <span className="text-destructive">*</span>
              </Label>
              <Input id="invoice-date" placeholder="۱۴۰۵/۰۵/۰۸" />
            </div>

            <div className="space-y-2">
              <Label htmlFor="payment-method">نحوه پرداخت</Label>
              <Select dir="rtl" defaultValue="cash">
                <SelectTrigger id="payment-method" className="w-full">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="cash">نقدی</SelectItem>
                  <SelectItem value="credit">اعتباری / چک</SelectItem>
                  <SelectItem value="installment">اقساطی</SelectItem>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="notes">توضیحات</Label>
              <Textarea id="notes" placeholder="توضیحات تکمیلی فاکتور را وارد کنید..." rows={4} />
            </div>

            <div className="flex items-center justify-end gap-2 border-t border-border/60 pt-5 md:col-span-2">
              <Button type="button" variant="outline">
                انصراف
              </Button>
              <Button type="submit">
                <Save />
                ثبت فاکتور فروش
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </>
  );
}
