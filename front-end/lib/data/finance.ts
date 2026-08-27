export interface CashBankAccount {
  id: string
  accountType: string
  accountName: string
  balance: number
  lastActivity: string
}

export const cashBankAccounts: CashBankAccount[] = [
  { id: "ACC-01", accountType: "حساب جاری", accountName: "بانک ملت - شعبه مرکزی", balance: 1284500000, lastActivity: "۱۴۰۵/۰۵/۰۸" },
  { id: "ACC-02", accountType: "حساب جاری", accountName: "بانک تجارت - شعبه ونک", balance: 642300000, lastActivity: "۱۴۰۵/۰۵/۰۷" },
  { id: "ACC-03", accountType: "صندوق نقدی", accountName: "صندوق دفتر مرکزی", balance: 58600000, lastActivity: "۱۴۰۵/۰۵/۰۸" },
  { id: "ACC-04", accountType: "حساب پس‌انداز", accountName: "بانک ملت - سپرده کوتاه‌مدت", balance: 950000000, lastActivity: "۱۴۰۵/۰۴/۳۰" },
  { id: "ACC-05", accountType: "صندوق نقدی", accountName: "صندوق کارخانه", balance: 21400000, lastActivity: "۱۴۰۵/۰۵/۰۶" },
]

export interface FinanceRecord {
  id: string
  description: string
  type: "income" | "expense"
  category: string
  amount: number
  date: string
}

export const financeRecords: FinanceRecord[] = [
  { id: "FN-301", description: "دریافت وجه فاکتور #۱۰۴۵۲", type: "income", category: "فروش", amount: 85200000, date: "۱۴۰۵/۰۵/۰۸" },
  { id: "FN-300", description: "پرداخت به تامین‌کننده فولاد البرز", type: "expense", category: "خرید مواد اولیه", amount: 120000000, date: "۱۴۰۵/۰۵/۰۷" },
  { id: "FN-299", description: "دریافت وجه فاکتور #۱۰۴۵۱", type: "income", category: "فروش", amount: 42900000, date: "۱۴۰۵/۰۵/۰۷" },
  { id: "FN-298", description: "پرداخت حقوق و دستمزد مرداد", type: "expense", category: "منابع انسانی", amount: 68500000, date: "۱۴۰۵/۰۵/۰۵" },
  { id: "FN-297", description: "پرداخت قبض برق کارخانه", type: "expense", category: "هزینه‌های جاری", amount: 18400000, date: "۱۴۰۵/۰۵/۰۴" },
  { id: "FN-296", description: "دریافت وجه فاکتور #۱۰۴۵۰", type: "income", category: "فروش", amount: 29600000, date: "۱۴۰۵/۰۵/۰۴" },
  { id: "FN-295", description: "پرداخت به تامین‌کننده پلیمر کیمیا", type: "expense", category: "خرید مواد اولیه", amount: 95300000, date: "۱۴۰۵/۰۵/۰۳" },
  { id: "FN-294", description: "پرداخت اجاره انبار مرکزی", type: "expense", category: "هزینه‌های جاری", amount: 42000000, date: "۱۴۰۵/۰۵/۰۲" },
  { id: "FN-293", description: "دریافت وجه فاکتور #۱۰۴۴۹", type: "income", category: "فروش", amount: 55000000, date: "۱۴۰۵/۰۵/۰۱" },
  { id: "FN-292", description: "سود سپرده کوتاه‌مدت", type: "income", category: "سایر درآمدها", amount: 12300000, date: "۱۴۰۵/۰۴/۳۰" },
]
