"use client"

import Link from "next/link"
import { LogOut, Settings, User, LifeBuoy, ChevronsUpDown } from "lucide-react"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

const currentUser = {
  name: "سارا محمدی",
  role: "مدیر عملیات",
  email: "s.mohammadi@arvin-erp.ir",
  initials: "س‌م",
}

export function UserNav() {
  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <button
          type="button"
          className="flex items-center gap-2 rounded-lg py-1 ps-1 pe-2 transition-colors hover:bg-accent"
        >
          <Avatar className="size-8 border border-border/60">
            <AvatarFallback className="bg-gradient-to-br from-primary/30 to-chart-5/30 text-xs text-foreground">
              {currentUser.initials}
            </AvatarFallback>
          </Avatar>
          <span className="hidden flex-col items-start leading-tight sm:flex">
            <span className="text-xs font-medium text-foreground">{currentUser.name}</span>
            <span className="text-[11px] text-muted-foreground">{currentUser.role}</span>
          </span>
          <ChevronsUpDown className="hidden size-3.5 text-muted-foreground sm:block" />
        </button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-64">
        <DropdownMenuLabel className="font-normal">
          <div className="flex flex-col gap-0.5 px-1 py-1">
            <span className="text-sm font-medium text-foreground">{currentUser.name}</span>
            <span className="text-xs text-muted-foreground" dir="ltr">
              {currentUser.email}
            </span>
          </div>
        </DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuGroup>
          <DropdownMenuItem asChild>
            <Link href="#">
              <User />
              پروفایل من
            </Link>
          </DropdownMenuItem>
          <DropdownMenuItem asChild>
            <Link href="#">
              <Settings />
              تنظیمات حساب
            </Link>
          </DropdownMenuItem>
          <DropdownMenuItem asChild>
            <Link href="#">
              <LifeBuoy />
              پشتیبانی
            </Link>
          </DropdownMenuItem>
        </DropdownMenuGroup>
        <DropdownMenuSeparator />
        <DropdownMenuItem variant="destructive">
          <LogOut />
          خروج از حساب کاربری
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
