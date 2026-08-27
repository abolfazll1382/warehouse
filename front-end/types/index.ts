import type { LucideIcon } from "lucide-react";

/** A single leaf link inside the sidebar / command palette. */
export interface NavItem {
  title: string;
  href: string;
  description?: string;
}

/** A top-level sidebar entry. Either a direct link, or a group with children rendered in an accordion. */
export interface NavGroup {
  id: string;
  title: string;
  icon: LucideIcon;
  href?: string;
  items?: NavItem[];
}

/** Generic status used across list/table pages (orders, invoices, payroll runs, etc.) */
export type RecordStatus =
  | "completed"
  | "processing"
  | "pending"
  | "failed"
  | "active"
  | "inactive"
  | "low-stock";

export interface StatusMeta {
  label: string;
  className: string;
}

export interface Kpi {
  id: string;
  title: string;
  value: string;
  changeLabel: string;
  trend: "up" | "down";
  icon: LucideIcon;
  accent: "primary" | "success" | "warning" | "sky";
}

export interface Transaction {
  id: string;
  party: string;
  description: string;
  date: string;
  amount: number;
  direction: "in" | "out";
  status: RecordStatus;
}

export interface MonthlyPoint {
  month: string;
  sales: number;
  orders: number;
}

export interface TopProduct {
  id: string;
  name: string;
  category: string;
  share: number; // percentage of total sales, 0-100
  amount: number;
}
