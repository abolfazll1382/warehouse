"use client";

import Link from "next/link";
import { Boxes, PanelRightClose, PanelRightOpen } from "lucide-react";
import { useSidebar } from "@/components/layout/sidebar-provider";
import { SidebarNav } from "@/components/layout/sidebar-nav";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Sheet, SheetContent, SheetHeader, SheetTitle } from "@/components/ui/sheet";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { cn } from "@/lib/utils";

function SidebarBrand({ collapsed }: { collapsed: boolean }) {
  return (
    <Link
      href="/"
      className={cn(
        "flex h-16 shrink-0 items-center gap-2.5 px-4",
        collapsed && "justify-center px-0"
      )}
    >
      <span className="flex size-8 shrink-0 items-center justify-center rounded-lg bg-gradient-to-br from-primary to-chart-5 text-primary-foreground shadow-lg shadow-primary/20">
        <Boxes className="size-[18px]" />
      </span>
      {!collapsed && (
        <span className="flex flex-col leading-tight">
          <span className="text-sm font-bold text-sidebar-foreground">آروین</span>
          <span className="text-[11px] text-muted-foreground">سامانه یکپارچه سازمانی</span>
        </span>
      )}
    </Link>
  );
}

export function Sidebar() {
  const { collapsed, toggleCollapsed, mobileOpen, setMobileOpen } = useSidebar();

  return (
    <>
      {/* Desktop rail — fixed to the right edge (inline-start in RTL) */}
      <aside
        className={cn(
          "fixed inset-y-0 start-0 z-40 hidden flex-col border-e border-sidebar-border bg-sidebar/90 backdrop-blur-xl transition-[width] duration-200 ease-in-out lg:flex",
          collapsed ? "w-[72px]" : "w-64"
        )}
      >
        <SidebarBrand collapsed={collapsed} />
        <ScrollArea className="min-h-0 flex-1">
          <SidebarNav collapsed={collapsed} />
        </ScrollArea>
        <div className="flex shrink-0 items-center justify-center border-t border-sidebar-border p-2">
          <Tooltip>
            <TooltipTrigger asChild>
              <button
                type="button"
                onClick={toggleCollapsed}
                className="flex size-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:bg-sidebar-accent hover:text-sidebar-foreground"
              >
                {collapsed ? (
                  <PanelRightOpen className="size-[18px]" />
                ) : (
                  <PanelRightClose className="size-[18px]" />
                )}
                <span className="sr-only">جمع‌کردن / باز کردن منو</span>
              </button>
            </TooltipTrigger>
            <TooltipContent side="left">
              {collapsed ? "باز کردن منو" : "جمع‌کردن منو"}
            </TooltipContent>
          </Tooltip>
        </div>
      </aside>

      {/* Mobile off-canvas menu */}
      <Sheet open={mobileOpen} onOpenChange={setMobileOpen}>
        <SheetContent side="right" className="flex w-72 flex-col gap-0 p-0">
          <SheetHeader className="sr-only">
            <SheetTitle>منوی ناوبری</SheetTitle>
          </SheetHeader>
          <SidebarBrand collapsed={false} />
          <ScrollArea className="min-h-0 flex-1">
            <SidebarNav collapsed={false} onNavigate={() => setMobileOpen(false)} />
          </ScrollArea>
        </SheetContent>
      </Sheet>
    </>
  );
}
