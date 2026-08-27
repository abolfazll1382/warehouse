export interface InventoryItem {
  id: string
  name: string
  category: string
  quantity: number
  unit: string
  status: "in-stock" | "low-stock" | "out-of-stock"
}

export const inventoryItems: InventoryItem[] = [
  { id: "INV-P-001", name: "پروفیل آلومینیومی ۶۰۶۰", category: "پروفیل", quantity: 2450, unit: "متر", status: "in-stock" },
  { id: "INV-P-002", name: "پروفیل آلومینیومی ۴۰۴۰", category: "پروفیل", quantity: 1380, unit: "متر", status: "in-stock" },
  { id: "INV-S-011", name: "ورق فولادی گالوانیزه ۱ میل", category: "ورق فلزی", quantity: 96, unit: "برگ", status: "low-stock" },
  { id: "INV-C-005", name: "لوله مسی صنعتی ۱۵ میل", category: "لوله و اتصالات", quantity: 640, unit: "متر", status: "in-stock" },
  { id: "INV-H-021", name: "یراق‌آلات درب ضدسرقت", category: "یراق‌آلات", quantity: 38, unit: "دست", status: "low-stock" },
  { id: "INV-H-022", name: "دستگیره و قفل پنجره", category: "یراق‌آلات", quantity: 512, unit: "عدد", status: "in-stock" },
  { id: "INV-PT-003", name: "رنگ پودری الکترواستاتیک - مشکی", category: "پوشش و رنگ", quantity: 0, unit: "کیلوگرم", status: "out-of-stock" },
  { id: "INV-PT-004", name: "رنگ پودری الکترواستاتیک - سفید", category: "پوشش و رنگ", quantity: 340, unit: "کیلوگرم", status: "in-stock" },
  { id: "INV-G-014", name: "شیشه دوجداره لمینت", category: "شیشه", quantity: 210, unit: "متر مربع", status: "in-stock" },
  { id: "INV-R-009", name: "واشر و نوار درزگیر EPDM", category: "قطعات جانبی", quantity: 74, unit: "رول", status: "low-stock" },
  { id: "INV-P-006", name: "پروفیل یو‌پی‌وی‌سی ۵ کاناله", category: "پروفیل", quantity: 890, unit: "متر", status: "in-stock" },
  { id: "INV-S-016", name: "پیچ و مهره صنعتی ضدزنگ", category: "قطعات جانبی", quantity: 4200, unit: "عدد", status: "in-stock" },
]
