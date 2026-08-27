export interface Customer {
  id: string
  name: string
  phone: string
  city: string
  totalPurchases: number
  status: "active" | "inactive"
}

export const customers: Customer[] = [
  { id: "CUS-01", name: "شرکت داتیس صنعت", phone: "۰۲۱-۸۸۴۴۱۱۲۲", city: "تهران", totalPurchases: 685000000, status: "active" },
  { id: "CUS-02", name: "فروشگاه زنجیره‌ای رفاه‌گستر", phone: "۰۲۱-۴۴۵۵۶۶۷۷", city: "تهران", totalPurchases: 412000000, status: "active" },
  { id: "CUS-03", name: "بازرگانی پارسیان تجارت", phone: "۰۳۱-۳۲۲۳۴۴۵۵", city: "اصفهان", totalPurchases: 298000000, status: "active" },
  { id: "CUS-04", name: "شرکت کیان تجارت آسیا", phone: "۰۵۱-۳۸۸۹۹۰۰۱", city: "مشهد", totalPurchases: 356500000, status: "active" },
  { id: "CUS-05", name: "گروه ساختمانی نوین‌سازه", phone: "۰۲۱-۲۲۱۱۳۳۴۴", city: "کرج", totalPurchases: 890000000, status: "active" },
  { id: "CUS-06", name: "فروشگاه درب و پنجره آریا", phone: "۰۷۱-۳۲۴۴۵۵۶۶", city: "شیراز", totalPurchases: 154000000, status: "active" },
  { id: "CUS-07", name: "شرکت تعاونی مسکن البرز", phone: "۰۲۶-۳۲۲۳۴۴۵۵", city: "کرج", totalPurchases: 62000000, status: "inactive" },
  { id: "CUS-08", name: "نمایندگی تهویه و نما", phone: "۰۴۱-۳۳۴۴۵۵۶۶", city: "تبریز", totalPurchases: 208000000, status: "active" },
  { id: "CUS-09", name: "بازرگانی خلیج فارس", phone: "۰۷۷-۳۳۲۲۱۱۰۰", city: "بندرعباس", totalPurchases: 133500000, status: "active" },
  { id: "CUS-10", name: "شرکت عمران و نما گستر", phone: "۰۲۱-۷۷۸۸۹۹۰۰", city: "تهران", totalPurchases: 521000000, status: "active" },
]

export interface Invoice {
  id: string
  customer: string
  date: string
  amount: number
  status: "completed" | "pending" | "processing" | "failed"
}

export const invoices: Invoice[] = [
  { id: "INV-10452", customer: "شرکت داتیس صنعت", date: "۱۴۰۵/۰۵/۰۸", amount: 85200000, status: "completed" },
  { id: "INV-10451", customer: "فروشگاه زنجیره‌ای رفاه‌گستر", date: "۱۴۰۵/۰۵/۰۷", amount: 42900000, status: "completed" },
  { id: "INV-10450", customer: "بازرگانی پارسیان تجارت", date: "۱۴۰۵/۰۵/۰۴", amount: 29600000, status: "pending" },
  { id: "INV-10449", customer: "شرکت کیان تجارت آسیا", date: "۱۴۰۵/۰۵/۰۱", amount: 55000000, status: "completed" },
  { id: "INV-10448", customer: "گروه ساختمانی نوین‌سازه", date: "۱۴۰۵/۰۴/۲۸", amount: 214000000, status: "completed" },
  { id: "INV-10447", customer: "فروشگاه درب و پنجره آریا", date: "۱۴۰۵/۰۴/۲۵", amount: 38700000, status: "processing" },
  { id: "INV-10446", customer: "نمایندگی تهویه و نما", date: "۱۴۰۵/۰۴/۲۱", amount: 61500000, status: "completed" },
  { id: "INV-10445", customer: "شرکت عمران و نما گستر", date: "۱۴۰۵/۰۴/۱۷", amount: 97300000, status: "failed" },
  { id: "INV-10444", customer: "بازرگانی خلیج فارس", date: "۱۴۰۵/۰۴/۱۴", amount: 33500000, status: "completed" },
]
