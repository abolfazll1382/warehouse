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
import { suppliers } from "@/lib/data/purchasing";
import { PackagePlus } from "lucide-react";

const categories = ["پروفیل", "ورق فلزی", "لوله و اتصالات", "یراق‌آلات", "پوشش و رنگ", "شیشه", "قطعات جانبی"];
const units = ["متر", "کیلوگرم", "عدد", "برگ", "رول", "متر مربع", "دست"];

export default function InventoryAddPage() {
  return (
    <>
      <PageHeader title="افزودن کالا به انبار" description="ثبت رسید ورود کالا و افزایش موجودی انبار" />

      <Card className="mx-auto max-w-3xl">
        <CardHeader>
          <CardTitle>اطلاعات رسید ورود کالا</CardTitle>
          <CardDescription>فیلدهای ستاره‌دار تکمیل آن‌ها الزامی است.</CardDescription>
        </CardHeader>
        <CardContent>
          <form className="grid grid-cols-1 gap-x-4 gap-y-5 md:grid-cols-2">
            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="item-name">
                نام کالا <span className="text-destructive">*</span>
              </Label>
              <Input id="item-name" placeholder="مثال: پروفیل آلومینیومی ۶۰۶۰" />
            </div>

            <div className="space-y-2">
              <Label htmlFor="category">
                دسته‌بندی <span className="text-destructive">*</span>
              </Label>
              <Select dir="rtl">
                <SelectTrigger id="category" className="w-full">
                  <SelectValue placeholder="انتخاب دسته‌بندی..." />
                </SelectTrigger>
                <SelectContent>
                  {categories.map((c) => (
                    <SelectItem key={c} value={c}>
                      {c}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="supplier">تامین‌کننده</Label>
              <Select dir="rtl">
                <SelectTrigger id="supplier" className="w-full">
                  <SelectValue placeholder="انتخاب تامین‌کننده..." />
                </SelectTrigger>
                <SelectContent>
                  {suppliers.map((s) => (
                    <SelectItem key={s.id} value={s.id}>
                      {s.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="quantity">
                مقدار ورودی <span className="text-destructive">*</span>
              </Label>
              <Input id="quantity" type="number" placeholder="۰" min={0} />
            </div>

            <div className="space-y-2">
              <Label htmlFor="unit">
                واحد اندازه‌گیری <span className="text-destructive">*</span>
              </Label>
              <Select dir="rtl">
                <SelectTrigger id="unit" className="w-full">
                  <SelectValue placeholder="انتخاب واحد..." />
                </SelectTrigger>
                <SelectContent>
                  {units.map((u) => (
                    <SelectItem key={u} value={u}>
                      {u}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="receipt-date">
                تاریخ رسید <span className="text-destructive">*</span>
              </Label>
              <Input id="receipt-date" placeholder="۱۴۰۵/۰۵/۰۸" className="md:max-w-56" />
            </div>

            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="notes">توضیحات</Label>
              <Textarea id="notes" placeholder="توضیحات تکمیلی رسید انبار را وارد کنید..." rows={4} />
            </div>

            <div className="flex items-center justify-end gap-2 border-t border-border/60 pt-5 md:col-span-2">
              <Button type="button" variant="outline">
                انصراف
              </Button>
              <Button type="submit">
                <PackagePlus />
                ثبت رسید ورود کالا
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </>
  );
}
