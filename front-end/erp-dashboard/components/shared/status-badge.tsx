import { Badge } from "@/components/ui/badge"
import { cn } from "@/lib/utils"

type Tone = "success" | "warning" | "destructive" | "secondary" | "sky"

const toneClasses: Record<Tone, string> = {
  success: "bg-success/15 text-success",
  warning: "bg-warning/15 text-warning",
  destructive: "bg-destructive/15 text-destructive",
  secondary: "bg-secondary text-secondary-foreground",
  sky: "bg-chart-5/15 text-chart-5",
}

// Central registry so every module (HR, production, sales...) renders the
// same status vocabulary consistently instead of ad-hoc strings per page.
const STATUS_MAP: Record<string, { label: string; tone: Tone }> = {
  completed: { label: "تکمیل‌شده", tone: "success" },
  processing: { label: "در حال پردازش", tone: "sky" },
  pending: { label: "در انتظار", tone: "warning" },
  failed: { label: "ناموفق", tone: "destructive" },
  active: { label: "فعال", tone: "success" },
  inactive: { label: "غیرفعال", tone: "secondary" },
  passed: { label: "تایید شده", tone: "success" },
  review: { label: "نیازمند بازبینی", tone: "warning" },
  "in-stock": { label: "موجود", tone: "success" },
  "low-stock": { label: "رو به اتمام", tone: "warning" },
  "out-of-stock": { label: "ناموجود", tone: "destructive" },
}

export function StatusBadge({ status }: { status: string }) {
  const meta = STATUS_MAP[status] ?? { label: status, tone: "secondary" as Tone }
  return (
    <Badge variant="outline" className={cn("border-transparent font-medium", toneClasses[meta.tone])}>
      {meta.label}
    </Badge>
  )
}
