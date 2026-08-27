import type { Metadata, Viewport } from "next";
import "@fontsource-variable/vazirmatn/wght.css";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "سامانه مدیریت یکپارچه آروین",
    template: "%s | آروین ERP",
  },
  description:
    "داشبورد مدیریت یکپارچه سازمانی برای منابع انسانی، تولید، خرید، فروش، انبار و امور مالی.",
};

export const viewport: Viewport = {
  themeColor: "#09090b",
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="fa" dir="rtl" className="dark">
      <body className="relative min-h-screen bg-background font-sans text-foreground antialiased">
        {/* Ambient decorative glow — fixed behind everything, gives the glass
            panels (header/sidebar/popovers) something to actually catch. */}
        <div
          aria-hidden
          className="pointer-events-none fixed inset-0 z-0 overflow-hidden"
        >
          <div className="absolute -top-40 -start-40 h-[32rem] w-[32rem] rounded-full bg-primary/20 blur-[120px]" />
          <div className="absolute top-1/3 -end-52 h-[28rem] w-[28rem] rounded-full bg-chart-2/10 blur-[130px]" />
          <div className="absolute bottom-0 start-1/4 h-[24rem] w-[24rem] rounded-full bg-chart-4/10 blur-[130px]" />
        </div>
        <div className="relative z-10">{children}</div>
      </body>
    </html>
  );
}
