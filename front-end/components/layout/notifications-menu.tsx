"use client"

import { Bell, PackageCheck, ReceiptText, UserPlus, AlertTriangle } from "lucide-react"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { cn } from "@/lib/utils"

const notifications = [
  {
    id: "n1",
    icon: ReceiptText,
    title: "فاکتور جدید صادر شد",
    description: "فاکتور شماره ۱۰۴۵۲ برای شرکت داتیس صادر شد.",
    time: "۱۰ دقیقه پیش",
    unread: true,
  },
  {
    id: "n2",
    icon: AlertTriangle,
    title: "هشدار موجودی انبار",
    description: "موجودی «پروفیل آلومینیومی ۶۰۶۰» به زیر حد مجاز رسید.",
    time: "۱ ساعت پیش",
    unread: true,
  },
  {
    id: "n3",
    icon: PackageCheck,
    title: "سفارش خرید تایید شد",
    description: "سفارش خرید PO-2288 توسط مدیر خرید تایید شد.",
    time: "۳ ساعت پیش",
    unread: true,
  },
  {
    id: "n4",
    icon: UserPlus,
    title: "پرسنل جدید",
    description: "«علی رضایی» به‌عنوان کارشناس تولید ثبت شد.",
    time: "دیروز",
    unread: false,
  },
]

export function NotificationsMenu() {
  const unreadCount = notifications.filter((n) => n.unread).length

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <button
          type="button"
          className="relative flex size-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
        >
          <Bell className="size-[18px]" />
          {unreadCount > 0 && (
            <span className="absolute end-1.5 top-1.5 flex size-2 rounded-full bg-destructive ring-2 ring-background" />
          )}
          <span className="sr-only">اعلان‌ها</span>
        </button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-80 p-0">
        <div className="flex items-center justify-between px-3 py-2.5">
          <DropdownMenuLabel className="p-0 text-sm font-semibold text-foreground">
            اعلان‌ها
          </DropdownMenuLabel>
          <span className="text-xs text-muted-foreground">{unreadCount} مورد جدید</span>
        </div>
        <DropdownMenuSeparator className="m-0" />
        <div className="max-h-80 overflow-y-auto scrollbar-thin py-1">
          {notifications.map((n) => (
            <DropdownMenuItem key={n.id} className="items-start gap-3 rounded-none px-3 py-2.5">
              <span
                className={cn(
                  "mt-0.5 flex size-8 shrink-0 items-center justify-center rounded-full",
                  n.unread ? "bg-primary/15 text-primary" : "bg-muted text-muted-foreground"
                )}
              >
                <n.icon className="size-4" />
              </span>
              <span className="flex flex-1 flex-col gap-0.5 text-start whitespace-normal">
                <span className="flex items-center gap-1.5 text-xs font-medium text-foreground">
                  {n.title}
                  {n.unread && <span className="size-1.5 rounded-full bg-primary" />}
                </span>
                <span className="text-xs text-muted-foreground">{n.description}</span>
                <span className="text-[11px] text-muted-foreground/70">{n.time}</span>
              </span>
            </DropdownMenuItem>
          ))}
        </div>
        <DropdownMenuSeparator className="m-0" />
        <DropdownMenuItem className="justify-center rounded-none py-2.5 text-xs font-medium text-primary">
          مشاهده همه اعلان‌ها
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
