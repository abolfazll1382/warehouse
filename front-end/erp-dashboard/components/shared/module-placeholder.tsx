import Link from "next/link"
import { ArrowLeft, type LucideIcon } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Skeleton } from "@/components/ui/skeleton"

/**
 * Reusable "next phase" state for action/form-oriented sub-pages
 * (registration & issuance flows) that are scoped for a later iteration.
 * Keeps every not-yet-built route on-brand instead of 404ing.
 */
export function ModulePlaceholder({
  icon: Icon,
  title,
  description,
}: {
  icon: LucideIcon
  title: string
  description: string
}) {
  return (
    <Card className="overflow-hidden">
      <CardContent className="flex flex-col items-center gap-5 px-6 py-16 text-center">
        <span className="flex size-14 items-center justify-center rounded-2xl bg-primary/10 text-primary">
          <Icon className="size-7" />
        </span>
        <div className="max-w-md space-y-1.5">
          <h2 className="text-base font-semibold text-foreground">{title}</h2>
          <p className="text-sm text-muted-foreground">{description}</p>
        </div>
        <div className="mt-1 flex w-full max-w-xs flex-col gap-2 opacity-40">
          <Skeleton className="h-9 w-full" />
          <Skeleton className="h-9 w-full" />
        </div>
        <Button asChild variant="outline" size="sm" className="mt-2">
          <Link href="/">
            <ArrowLeft className="rtl:rotate-180" />
            بازگشت به داشبورد
          </Link>
        </Button>
      </CardContent>
    </Card>
  )
}
