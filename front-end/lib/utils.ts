import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

/**
 * Merges Tailwind class names intelligently, resolving conflicts
 * (e.g. "px-2 px-4" -> "px-4") while preserving conditional classes.
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Formats a number using Persian (Eastern Arabic) numerals and
 * Persian digit grouping — used across KPI cards, tables and charts
 * so figures read naturally for a Farsi-speaking audience.
 */
export function formatNumber(value: number): string {
  return new Intl.NumberFormat("fa-IR").format(value);
}

/**
 * Formats a Rial/Toman amount with the "تومان" suffix and Persian numerals.
 */
export function formatToman(value: number): string {
  return `${formatNumber(value)} تومان`;
}

/**
 * Formats a signed percentage change with Persian numerals, e.g. "۱۲.۵٪+"
 * Returns the sign, formatted value and "٪" independently so callers can
 * style them (color-coding positive/negative) without re-parsing.
 */
export function formatPercent(value: number): string {
  const formatted = new Intl.NumberFormat("fa-IR", {
    maximumFractionDigits: 1,
    minimumFractionDigits: 0,
  }).format(Math.abs(value));
  return `${formatted}٪`;
}
