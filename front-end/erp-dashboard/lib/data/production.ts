export interface ProductionLine {
  id: string
  name: string
  product: string
  capacity: string
  efficiency: number
  status: "active" | "inactive" | "processing"
}

export const productionLines: ProductionLine[] = [
  { id: "PL-01", name: "خط تولید ۱ - اکستروژن", product: "پروفیل آلومینیومی درب و پنجره", capacity: "۴۲ تن/روز", efficiency: 91, status: "active" },
  { id: "PL-02", name: "خط تولید ۲ - رنگ پودری", product: "پوشش الکترواستاتیک پروفیل", capacity: "۳۰ تن/روز", efficiency: 84, status: "active" },
  { id: "PL-03", name: "خط تولید ۳ - برش و سوراخکاری", product: "قطعات یراق‌آلات فلزی", capacity: "۱۸,۰۰۰ قطعه/روز", efficiency: 76, status: "active" },
  { id: "PL-04", name: "خط تولید ۴ - مونتاژ", product: "مجموعه درب و پنجره آماده نصب", capacity: "۲۲۰ سری/روز", efficiency: 88, status: "active" },
  { id: "PL-05", name: "خط تولید ۵ - گالوانیزه", product: "ورق و پروفیل فولادی گالوانیزه", capacity: "۲۶ تن/روز", efficiency: 0, status: "inactive" },
  { id: "PL-06", name: "خط تولید ۶ - جوشکاری", product: "قاب‌های فلزی صنعتی", capacity: "۹۵ قاب/روز", efficiency: 69, status: "processing" },
]

export interface QualityCheck {
  id: string
  product: string
  date: string
  result: "passed" | "failed" | "review"
  inspector: string
}

export const qualityChecks: QualityCheck[] = [
  { id: "QC-1180", product: "پروفیل آلومینیومی ۶۰۶۰", date: "۱۴۰۵/۰۵/۰۸", result: "passed", inspector: "مریم صادقی" },
  { id: "QC-1179", product: "پوشش الکترواستاتیک - رنگ کوره‌ای", date: "۱۴۰۵/۰۵/۰۸", result: "passed", inspector: "مریم صادقی" },
  { id: "QC-1178", product: "یراق‌آلات درب ضدسرقت", date: "۱۴۰۵/۰۵/۰۷", result: "review", inspector: "حسین نوری" },
  { id: "QC-1177", product: "ورق فولادی گالوانیزه", date: "۱۴۰۵/۰۵/۰۶", result: "failed", inspector: "مریم صادقی" },
  { id: "QC-1176", product: "پروفیل آلومینیومی ۴۰۴۰", date: "۱۴۰۵/۰۵/۰۶", result: "passed", inspector: "کیوان یوسفی" },
  { id: "QC-1175", product: "مجموعه درب آماده نصب", date: "۱۴۰۵/۰۵/۰۵", result: "passed", inspector: "مریم صادقی" },
  { id: "QC-1174", product: "لوله مسی صنعتی", date: "۱۴۰۵/۰۵/۰۴", result: "passed", inspector: "حسین نوری" },
  { id: "QC-1173", product: "قاب فلزی صنعتی", date: "۱۴۰۵/۰۵/۰۳", result: "review", inspector: "مریم صادقی" },
]
