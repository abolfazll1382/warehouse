# آروین ERP — سامانه مدیریت یکپارچه سازمانی

پروتوتایپ UI یک داشبورد جامع ERP، ساخته‌شده با Next.js (App Router)، TypeScript، Tailwind CSS v4 و
الگوهای shadcn/ui. رابط کاربری کاملاً فارسی و راست‌به‌چپ (RTL) با تم تیره است.

## اجرای پروژه

```bash
npm install
npm run dev
```

سپس آدرس `http://localhost:3000` را در مرورگر باز کنید. برای build نهایی:

```bash
npm run build
npm run start
```

## پیاده‌سازی شده (MVP)

- **Layout**: سایدبار ثابت، جمع‌شونده و اسکرول‌پذیر (لبه راست، مطابق RTL) با آکاردئون ماژول‌ها +
  هدر با جستجو (Command Palette با `Ctrl/Cmd+K`)، اعلان‌ها، پروفایل کاربر و breadcrumb پویا.
- **نمای کلی (Overview)**: ۴ کارت KPI، نمودار Area تیره (recharts) با داده ماهانه بر اساس تقویم
  شمسی، ویجت پرفروش‌ترین محصولات، و جدول تراکنش‌های اخیر.
- **۷ ماژول کامل**: منابع انسانی، تولید، خرید، فروش، انبار و مالی — هرکدام با صفحات واقعی
  (نه Placeholder) روی یک کامپوننت DataTable قابل استفاده مجدد (مبتنی بر TanStack Table، شامل
  جستجو/مرتب‌سازی/صفحه‌بندی) به‌علاوه چند فرم ثبت اطلاعات.
- بیش از ۲۰ کامپوننت پایه به سبک shadcn/ui (Button, Card, Table, Accordion, DropdownMenu, Sheet,
  Select, Dialog, Command و…) که مستقیماً روی Radix UI ساخته شده‌اند.
- صفحات خطای ۴۰۴ / Error Boundary / Loading اختصاصی و هم‌راستا با تم تیره.
- فونت Vazirmatn (نسخه Variable، self-hosted) و پالت رنگی تیره با glassmorphism محدود به بخش‌های
  ناوبری (هدر/سایدبار)، نه کل رابط.

`npm run build` تست شده و بدون خطا (۱۷ مسیر) کامپایل و static generate می‌شود.

## ساختار پوشه‌ها

```
app/
  (dashboard)/          گروه مسیرهای پنل — layout مشترک با Sidebar + Header
    page.tsx            نمای کلی
    hr/ production/ purchasing/ sales/ inventory/ finance/
  layout.tsx             ریشه: html[dir=rtl][lang=fa]، فونت، پس‌زمینه
  globals.css            توکن‌های تم (Tailwind v4، CSS-first)
components/
  ui/                    پریمیتیوهای shadcn/ui
  layout/                Sidebar, Header, CommandMenu, Breadcrumb, UserNav...
  dashboard/             KpiCard, RevenueChart, RecentTransactions, TopProducts
  data-table/            DataTable عمومی + ستون قابل مرتب‌سازی
  hr/ production/ purchasing/ sales/ inventory/ finance/
                          کامپوننت‌های جدول/فرم مخصوص هر ماژول (Client Components)
  shared/                PageHeader, StatusBadge, ModulePlaceholder
lib/
  data/                  داده‌های نمونه (mock) به تفکیک ماژول
  nav-config.ts           منبع واحد ناوبری — Sidebar/Breadcrumb/Command Menu از همین‌جا می‌خوانند
  utils.ts                cn() + فرمت اعداد و مبالغ با ارقام فارسی
types/                   تایپ‌های مشترک TypeScript
```

## نکات فنی و تصمیم‌های معماری

- **جداسازی Server/Client**: صفحات پیش‌فرض Server Component هستند و فقط داده را از `lib/data`
  وارد کرده و به کامپوننت‌های تعاملی (`"use client"`) در `components/<module>/` پاس می‌دهند —
  الگوی صحیح برای اتصال بعدی به API واقعی.
- **RTL واقعی، نه فقط `dir="rtl"`**: سایدبار روی لبه فیزیکی راست قرار دارد، از کلاس‌های منطقی
  Tailwind (`ms-*`, `me-*`, `ps-*`, `pe-*`, `start-*`, `end-*`) به‌جای `left/right` استفاده شده،
  و آیکون‌های جهت‌دار (breadcrumb، صفحه‌بندی) به‌درستی برای RTL انتخاب/چرخانده شده‌اند.
- **TypeScript 6.0.3** (به‌جای 7.x) و بدون `experimental.useTypeScriptCli` — انتخابی آگاهانه برای
  سازگاری کامل با کل زنجیره ابزار Next.js 16، نه صرفاً جدیدترین نسخه.

## باقی‌مانده برای فازهای بعدی

- پیکربندی ESLint: نسخه فعلی `eslint-config-next` (و لایه‌ی سازگاری Flat Config آن) با
  ESLint 10 به یک باگ شناخته‌شده (`Converting circular structure to JSON`) برخورد می‌کند. فعلاً
  از پروژه حذف شده تا خروجی تمیز بماند؛ در فاز بعد یا با پایین آوردن نسخه ابزار یا با انتظار برای
  رفع باگ در آپ‌استریم قابل بازگردانی است.
- اتصال به API واقعی به‌جای داده‌های نمونه در `lib/data/*`.
- افزودن اعتبارسنجی فرم (react-hook-form + zod) به فرم‌های ثبت فروش/ورود/خروج کالا.
- احراز هویت و مدیریت نقش‌های کاربری.
