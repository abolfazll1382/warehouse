"use client";

import { Menu, Search } from "lucide-react";
import { useSidebar } from "@/components/layout/sidebar-provider";
import { useCommandMenu } from "@/components/layout/command-menu";
import { BreadcrumbNav } from "@/components/layout/breadcrumb-nav";
import { NotificationsMenu } from "@/components/layout/notifications-menu";
import { UserNav } from "@/components/layout/user-nav";
import { Button } from "@/components/ui/button";
import { Separator } from "@/components/ui/separator";

export function Header() {
  const { setMobileOpen } = useSidebar();
  const { setOpen: setCommandOpen } = useCommandMenu();

  return (
    <header className="glass-panel sticky top-0 z-30 flex h-16 shrink-0 items-center gap-3 border-b border-border/60 px-4 md:px-6 lg:px-8">
      <div className="flex flex-1 items-center gap-3">
        <Button
          variant="ghost"
          size="icon"
          className="lg:hidden"
          onClick={() => setMobileOpen(true)}
        >
          <Menu className="size-[18px]" />
          <span className="sr-only">باز کردن منو</span>
        </Button>
        <BreadcrumbNav />
      </div>

      <div className="flex items-center gap-1.5 sm:gap-2">
        <button
          type="button"
          onClick={() => setCommandOpen(true)}
          className="flex w-40 items-center gap-2 rounded-lg border border-input bg-secondary/40 px-3 py-1.5 text-sm text-muted-foreground transition-colors hover:border-ring/50 hover:bg-secondary/60 sm:w-56 md:w-72"
        >
          <Search className="size-4 shrink-0" />
          <span className="hidden truncate sm:inline">جستجو در سامانه...</span>
          <kbd
            dir="ltr"
            className="ms-auto hidden shrink-0 items-center gap-0.5 rounded border border-border/60 bg-background/60 px-1.5 py-0.5 font-mono text-[10px] text-muted-foreground sm:flex"
          >
            Ctrl K
          </kbd>
        </button>

        <NotificationsMenu />
        <Separator orientation="vertical" className="mx-1 hidden h-6 sm:block" />
        <UserNav />
      </div>
    </header>
  );
}
