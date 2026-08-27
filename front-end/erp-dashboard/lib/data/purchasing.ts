export interface Supplier {
  id: string
  name: string
  category: string
  contact: string
  rating: number
  status: "active" | "inactive"
}

export const suppliers: Supplier[] = [
  { id: "SUP-01", name: "فولاد البرز", category: "مواد اولیه فلزی", contact: "۰۲۱-۴۴۸۸۲۲۱۰", rating: 4.6, status: "active" },
  { id: "SUP-02", name: "پلیمر کیمیا", category: "مواد پلیمری", contact: "۰۲۱-۵۵۶۶۱۲۳۴", rating: 4.1, status: "active" },
  { id: "SUP-03", name: "رنگ و پوشش ایرانیان", category: "رنگ پودری", contact: "۰۳۱-۳۶۶۷۷۸۹۰", rating: 4.8, status: "active" },
  { id: "SUP-04", name: "یراق صنعت پارس", category: "یراق‌آلات", contact: "۰۲۱-۸۸۹۹۰۰۱۱", rating: 3.9, status: "active" },
  { id: "SUP-05", name: "آلومینیوم جنوب", category: "شمش و پروفیل آلومینیوم", contact: "۰۶۱-۳۳۴۴۵۵۶۶", rating: 4.4, status: "active" },
  { id: "SUP-06", name: "بسته‌بندی صنعتی نوین", category: "بسته‌بندی و حمل", contact: "۰۲۱-۲۲۳۳۴۴۵۵", rating: 3.6, status: "inactive" },
  { id: "SUP-07", name: "تجهیزات برشکاری آریا", category: "ابزار و تجهیزات", contact: "۰۲۶-۳۲۴۴۵۵۶۶", rating: 4.2, status: "active" },
]

export interface PurchaseOrder {
  id: string
  supplier: string
  date: string
  amount: number
  status: "completed" | "processing" | "pending" | "failed"
}

export const purchaseOrders: PurchaseOrder[] = [
  { id: "PO-2288", supplier: "فولاد البرز", date: "۱۴۰۵/۰۵/۰۷", amount: 120000000, status: "processing" },
  { id: "PO-2287", supplier: "پلیمر کیمیا", date: "۱۴۰۵/۰۵/۰۳", amount: 95300000, status: "failed" },
  { id: "PO-2286", supplier: "آلومینیوم جنوب", date: "۱۴۰۵/۰۴/۲۹", amount: 310000000, status: "completed" },
  { id: "PO-2285", supplier: "رنگ و پوشش ایرانیان", date: "۱۴۰۵/۰۴/۲۶", amount: 74500000, status: "completed" },
  { id: "PO-2284", supplier: "یراق صنعت پارس", date: "۱۴۰۵/۰۴/۲۲", amount: 58200000, status: "pending" },
  { id: "PO-2283", supplier: "تجهیزات برشکاری آریا", date: "۱۴۰۵/۰۴/۱۸", amount: 142000000, status: "completed" },
  { id: "PO-2282", supplier: "فولاد البرز", date: "۱۴۰۵/۰۴/۱۲", amount: 98700000, status: "completed" },
]
