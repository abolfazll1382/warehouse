import Link from "next/link";
import { Compass } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function NotFound() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center gap-5 bg-background px-6 text-center">
      <span className="flex size-16 items-center justify-center rounded-2xl bg-primary/10 text-primary">
        <Compass className="size-8" />
      </span>
      <div className="space-y-1.5">
        <p className="text-sm font-medium text-muted-foreground">خطای ۴۰۴</p>
        <h1 className="text-2xl font-bold text-foreground">صفحه مورد نظر یافت نشد</h1>
        <p className="text-sm text-muted-foreground">
          آدرس وارد شده در سامانه وجود ندارد یا جابه‌جا شده است.
        </p>
      </div>
      <Button asChild>
        <Link href="/">بازگشت به داشبورد</Link>
      </Button>
    </div>
  );
}
