export interface Personnel {
  id: string
  name: string
  position: string
  department: string
  hireDate: string
  status: "active" | "inactive"
}

export const personnel: Personnel[] = [
  { id: "EMP-001", name: "سارا محمدی", position: "مدیر عملیات", department: "عملیات", hireDate: "۱۳۹۹/۰۲/۱۲", status: "active" },
  { id: "EMP-002", name: "محمد حسینی", position: "مدیر منابع انسانی", department: "منابع انسانی", hireDate: "۱۳۹۸/۰۶/۰۱", status: "active" },
  { id: "EMP-003", name: "علی رضایی", position: "کارشناس تولید", department: "تولید", hireDate: "۱۴۰۲/۰۴/۱۵", status: "active" },
  { id: "EMP-004", name: "زهرا کریمی", position: "کارشناس مالی", department: "مالی", hireDate: "۱۴۰۱/۰۹/۰۹", status: "active" },
  { id: "EMP-005", name: "امیر تقوی", position: "کارشناس فروش", department: "فروش", hireDate: "۱۴۰۲/۱۱/۲۰", status: "active" },
  { id: "EMP-006", name: "فاطمه احمدی", position: "کارشناس خرید", department: "خرید", hireDate: "۱۴۰۰/۰۳/۰۵", status: "active" },
  { id: "EMP-007", name: "حسین نوری", position: "سرکارگر خط تولید", department: "تولید", hireDate: "۱۳۹۷/۰۷/۱۸", status: "active" },
  { id: "EMP-008", name: "مریم صادقی", position: "کارشناس کنترل کیفیت", department: "کنترل کیفیت", hireDate: "۱۴۰۱/۰۱/۳۰", status: "active" },
  { id: "EMP-009", name: "رضا جعفری", position: "انباردار", department: "انبار", hireDate: "۱۴۰۳/۰۵/۱۰", status: "active" },
  { id: "EMP-010", name: "نازنین قاسمی", position: "مدیر فروش", department: "فروش", hireDate: "۱۳۹۹/۱۲/۰۱", status: "active" },
  { id: "EMP-011", name: "کیوان یوسفی", position: "تکنسین تولید", department: "تولید", hireDate: "۱۴۰۴/۰۲/۰۸", status: "inactive" },
  { id: "EMP-012", name: "الهام رستمی", position: "کارشناس جذب و استخدام", department: "منابع انسانی", hireDate: "۱۴۰۳/۱۰/۱۴", status: "active" },
]

export interface PayrollRecord {
  id: string
  employee: string
  baseSalary: number
  insurance: number
  tax: number
  netPay: number
  status: "completed" | "pending" | "processing"
}

export const payroll: PayrollRecord[] = [
  { id: "PR-001", employee: "سارا محمدی", baseSalary: 62000000, insurance: 4340000, tax: 5100000, netPay: 52560000, status: "completed" },
  { id: "PR-002", employee: "محمد حسینی", baseSalary: 54000000, insurance: 3780000, tax: 4200000, netPay: 46020000, status: "completed" },
  { id: "PR-003", employee: "علی رضایی", baseSalary: 32000000, insurance: 2240000, tax: 1100000, netPay: 28660000, status: "completed" },
  { id: "PR-004", employee: "زهرا کریمی", baseSalary: 35000000, insurance: 2450000, tax: 1400000, netPay: 31150000, status: "completed" },
  { id: "PR-005", employee: "امیر تقوی", baseSalary: 30000000, insurance: 2100000, tax: 900000, netPay: 27000000, status: "processing" },
  { id: "PR-006", employee: "فاطمه احمدی", baseSalary: 33500000, insurance: 2345000, tax: 1250000, netPay: 29905000, status: "completed" },
  { id: "PR-007", employee: "حسین نوری", baseSalary: 38000000, insurance: 2660000, tax: 1700000, netPay: 33640000, status: "completed" },
  { id: "PR-008", employee: "مریم صادقی", baseSalary: 31000000, insurance: 2170000, tax: 1000000, netPay: 27830000, status: "pending" },
  { id: "PR-009", employee: "رضا جعفری", baseSalary: 27000000, insurance: 1890000, tax: 600000, netPay: 24510000, status: "completed" },
  { id: "PR-010", employee: "نازنین قاسمی", baseSalary: 48000000, insurance: 3360000, tax: 3300000, netPay: 41340000, status: "completed" },
]
