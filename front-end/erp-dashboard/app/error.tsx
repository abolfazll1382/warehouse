"use client";

import { useEffect } from "react";
import { TriangleAlert } from "lucide-react";
import { Button } from "@/components/ui/button";

export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <html lang="fa" dir="rtl" className="dark">
      <body className="flex min-h-screen flex-col items-center justify-center gap-5 bg-background px-6 text-center font-sans text-foreground antialiased">
        <span className="flex size-16 items-center justify-center rounded-2xl bg-destructive/10 text-destructive">
          <TriangleAlert className="size-8" />
        </span>
        <div className="space-y-1.5">
          <p className="text-sm font-medium text-muted-foreground">خطای غیرمنتظره</p>
          <h1 className="text-2xl font-bold text-foreground">مشکلی در نمایش صفحه پیش آمد</h1>
          <p className="text-sm text-muted-foreground">لطفاً دوباره تلاش کنید یا به داشبورد بازگردید.</p>
        </div>
        <Button onClick={() => reset()}>تلاش مجدد</Button>
      </body>
    </html>
  );
}
