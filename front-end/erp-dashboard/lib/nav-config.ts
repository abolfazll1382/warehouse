import {
  LayoutDashboard,
  Users,
  Factory,
  ShoppingCart,
  TrendingUp,
  Warehouse,
  Landmark,
} from "lucide-react";
import type { NavGroup } from "@/types";

/**
 * Single source of truth for the application's navigation tree.
 * Consumed by: <Sidebar />, <BreadcrumbNav />, and <CommandMenu />
 * so the three stay perfectly in sync as modules are added.
 */
export const navConfig: NavGroup[] = [
  {
    id: "dashboard",
    title: "داشبورد",
    icon: LayoutDashboard,
    href: "/",
  },
  {
    id: "hr",
    title: "منابع انسانی",
    icon: Users,
    items: [
      { title: "لیست پرسنل", href: "/hr/personnel", description: "مدیریت اطلاعات و وضعیت کارکنان" },
      { title: "حقوق و دستمزد", href: "/hr/payroll", description: "فیش‌های حقوقی و پرداخت‌های ماهانه" },
    ],
  },
  {
    id: "production",
    title: "تولید",
    icon: Factory,
    items: [
      { title: "خطوط تولید", href: "/production/lines", description: "وضعیت و بازدهی خطوط تولید کارخانه" },
      { title: "کنترل کیفیت", href: "/production/quality-control", description: "نتایج بازرسی و کنترل کیفیت محصولات" },
    ],
  },
  {
    id: "purchasing",
    title: "خرید",
    icon: ShoppingCart,
    items: [
      { title: "تامین‌کنندگان", href: "/purchasing/suppliers", description: "فهرست و رتبه‌بندی تامین‌کنندگان" },
      { title: "سفارشات خرید", href: "/purchasing/orders", description: "پیگیری سفارشات خرید ثبت‌شده" },
    ],
  },
  {
    id: "sales",
    title: "فروش",
    icon: TrendingUp,
    items: [
      { title: "ثبت فروش", href: "/sales/register", description: "ثبت فاکتور فروش جدید" },
      { title: "لیست مشتریان", href: "/sales/customers", description: "مدیریت اطلاعات مشتریان" },
      { title: "فاکتورها", href: "/sales/invoices", description: "فهرست فاکتورهای صادر شده" },
    ],
  },
  {
    id: "inventory",
    title: "انبار",
    icon: Warehouse,
    items: [
      { title: "لیست موجودی", href: "/inventory/list", description: "موجودی کالاها در انبار" },
      { title: "افزودن کالا به انبار", href: "/inventory/add", description: "ثبت رسید ورود کالا" },
      { title: "خروج / حذف کالا", href: "/inventory/issue", description: "ثبت حواله خروج کالا از انبار" },
    ],
  },
  {
    id: "finance",
    title: "مالی",
    icon: Landmark,
    items: [
      { title: "صندوق و بانک", href: "/finance/cash-bank", description: "مانده حساب‌های نقدی و بانکی" },
      { title: "درآمد و هزینه‌ها", href: "/finance/income-expense", description: "ثبت و مرور تراکنش‌های مالی" },
    ],
  },
];

/** Flat list of every navigable link — used by the command palette (⌘K) search. */
export const flatNavItems = navConfig.flatMap((group) =>
  group.href
    ? [{ title: group.title, href: group.href, groupTitle: group.title, icon: group.icon }]
    : (group.items ?? []).map((item) => ({
        title: item.title,
        href: item.href,
        groupTitle: group.title,
        icon: group.icon,
      }))
);

/** Looks up breadcrumb labels for a given pathname against the nav tree. */
export function findBreadcrumb(pathname: string) {
  for (const group of navConfig) {
    if (group.href === pathname) {
      return { group, item: null };
    }
    const item = group.items?.find((i) => i.href === pathname);
    if (item) return { group, item };
  }
  return null;
}
