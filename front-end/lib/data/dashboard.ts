import { Wallet, Package, Users, Clock } from "lucide-react";
import type { Kpi, MonthlyPoint, Transaction, TopProduct } from "@/types";

export const kpis: Kpi[] = [
  {
    id: "monthly-sales",
    title: "فروش کل ماهانه",
    value: "۴۸۲.۵ میلیون تومان",
    changeLabel: "۱۲.۴٪",
    trend: "up",
    icon: Wallet,
    accent: "success",
  },
  {
    id: "stock-items",
    title: "کالای موجود در انبار",
    value: "۳,۲۴۰ قلم",
    changeLabel: "۳.۲٪",
    trend: "up",
    icon: Package,
    accent: "sky",
  },
  {
    id: "active-employees",
    title: "کارمندان فعال",
    value: "۱۸۶ نفر",
    changeLabel: "۲.۲٪",
    trend: "up",
    icon: Users,
    accent: "primary",
  },
  {
    id: "pending-orders",
    title: "سفارشات در انتظار",
    value: "۴۲ سفارش",
    changeLabel: "۸٪",
    trend: "down",
    icon: Clock,
    accent: "warning",
  },
];

// Trailing 7 months on the Persian (Shamsi) calendar, ending in the current month.
// Farvardin (New Year) shows the seasonal Nowruz dip; Esfand shows the fiscal year-end push —
// both real patterns for an Iranian manufacturing business rather than generic noise.
export const monthlyData: MonthlyPoint[] = [
  { month: "بهمن", sales: 320, orders: 180 },
  { month: "اسفند", sales: 410, orders: 210 },
  { month: "فروردین", sales: 260, orders: 140 },
  { month: "اردیبهشت", sales: 350, orders: 175 },
  { month: "خرداد", sales: 395, orders: 190 },
  { month: "تیر", sales: 440, orders: 205 },
  { month: "مرداد", sales: 482, orders: 224 },
];

export const recentTransactions: Transaction[] = [
  {
    id: "1",
    party: "شرکت داتیس صنعت",
    description: "فاکتور فروش #۱۰۴۵۲",
    date: "۱۴۰۵/۰۵/۰۸",
    amount: 85200000,
    direction: "in",
    status: "completed",
  },
  {
    id: "2",
    party: "تامین‌کننده فولاد البرز",
    description: "سفارش خرید #PO-2288",
    date: "۱۴۰۵/۰۵/۰۷",
    amount: 120000000,
    direction: "out",
    status: "processing",
  },
  {
    id: "3",
    party: "فروشگاه زنجیره‌ای رفاه‌گستر",
    description: "فاکتور فروش #۱۰۴۵۱",
    date: "۱۴۰۵/۰۵/۰۷",
    amount: 42900000,
    direction: "in",
    status: "completed",
  },
  {
    id: "4",
    party: "واحد منابع انسانی",
    description: "پرداخت حقوق مرداد‌ماه",
    date: "۱۴۰۵/۰۵/۰۵",
    amount: 68500000,
    direction: "out",
    status: "completed",
  },
  {
    id: "5",
    party: "بازرگانی پارسیان تجارت",
    description: "فاکتور فروش #۱۰۴۵۰",
    date: "۱۴۰۵/۰۵/۰۴",
    amount: 29600000,
    direction: "in",
    status: "pending",
  },
  {
    id: "6",
    party: "تامین‌کننده پلیمر کیمیا",
    description: "خرید مواد اولیه پلیمری",
    date: "۱۴۰۵/۰۵/۰۳",
    amount: 95300000,
    direction: "out",
    status: "failed",
  },
  {
    id: "7",
    party: "شرکت کیان تجارت آسیا",
    description: "فاکتور فروش #۱۰۴۴۹",
    date: "۱۴۰۵/۰۵/۰۱",
    amount: 55000000,
    direction: "in",
    status: "completed",
  },
];

export const topProducts: TopProduct[] = [
  { id: "p1", name: "پروفیل آلومینیومی ۶۰۶۰", category: "پروفیل", share: 32, amount: 154400000 },
  { id: "p2", name: "ورق فولادی گالوانیزه", category: "ورق فلزی", share: 24, amount: 115800000 },
  { id: "p3", name: "لوله مسی صنعتی", category: "لوله و اتصالات", share: 18, amount: 86850000 },
  { id: "p4", name: "یراق‌آلات درب و پنجره", category: "یراق‌آلات", share: 14, amount: 67550000 },
  { id: "p5", name: "رنگ پودری الکترواستاتیک", category: "پوشش و رنگ", share: 12, amount: 57900000 },
];
