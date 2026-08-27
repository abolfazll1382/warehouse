"use client";

import * as React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { navConfig } from "@/lib/nav-config";
import { useSidebar } from "@/components/layout/sidebar-provider";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { cn } from "@/lib/utils";

export function SidebarNav({
  collapsed = false,
  onNavigate,
}: {
  collapsed?: boolean;
  onNavigate?: () => void;
}) {
  const pathname = usePathname();
  const { openGroupId, setOpenGroupId, openGroupAndExpand } = useSidebar();

  return (
    <nav className="flex flex-col gap-1 px-3 py-2">
      {navConfig.map((group) => {
        const Icon = group.icon;

        // Direct link entries (Dashboard / Overview) — no children to expand.
        if (group.href) {
          const active = pathname === group.href;
          const link = (
            <Link
              href={group.href}
              onClick={onNavigate}
              className={cn(
                "relative flex items-center gap-3 rounded-lg px-2.5 py-2 text-sm font-medium transition-colors",
                collapsed && "justify-center px-0 py-2.5",
                active
                  ? "bg-primary/10 text-primary"
                  : "text-sidebar-foreground/80 hover:bg-sidebar-accent hover:text-sidebar-foreground"
              )}
            >
              {active && (
                <span className="absolute inset-y-1 start-0 w-0.5 rounded-full bg-primary" />
              )}
              <Icon className="size-[18px] shrink-0" />
              {!collapsed && <span>{group.title}</span>}
            </Link>
          );

          if (!collapsed) return <div key={group.id}>{link}</div>;

          return (
            <Tooltip key={group.id}>
              <TooltipTrigger asChild>{link}</TooltipTrigger>
              <TooltipContent side="left">{group.title}</TooltipContent>
            </Tooltip>
          );
        }

        // Group entries with nested modules.
        const hasActiveChild = group.items?.some((i) => i.href === pathname);

        if (collapsed) {
          return (
            <Tooltip key={group.id}>
              <TooltipTrigger asChild>
                <button
                  type="button"
                  onClick={() => openGroupAndExpand(group.id)}
                  className={cn(
                    "relative flex items-center justify-center rounded-lg px-0 py-2.5 text-sm font-medium transition-colors",
                    hasActiveChild
                      ? "bg-primary/10 text-primary"
                      : "text-sidebar-foreground/80 hover:bg-sidebar-accent hover:text-sidebar-foreground"
                  )}
                >
                  {hasActiveChild && (
                    <span className="absolute inset-y-1 start-0 w-0.5 rounded-full bg-primary" />
                  )}
                  <Icon className="size-[18px] shrink-0" />
                </button>
              </TooltipTrigger>
              <TooltipContent side="left">{group.title}</TooltipContent>
            </Tooltip>
          );
        }

        return (
          <Accordion
            key={group.id}
            type="single"
            collapsible
            value={openGroupId ?? ""}
            onValueChange={(v) => setOpenGroupId(v || null)}
          >
            <AccordionItem value={group.id} className="border-b-0">
              <AccordionTrigger
                className={cn(
                  "rounded-lg px-2.5 py-2 hover:bg-sidebar-accent hover:no-underline",
                  hasActiveChild ? "text-primary" : "text-sidebar-foreground/80"
                )}
              >
                <span className="flex items-center gap-3">
                  <Icon className="size-[18px] shrink-0" />
                  {group.title}
                </span>
              </AccordionTrigger>
              <AccordionContent className="pb-1">
                <div className="flex flex-col gap-0.5 ps-[1.85rem]">
                  {group.items?.map((item) => {
                    const active = pathname === item.href;
                    return (
                      <Link
                        key={item.href}
                        href={item.href}
                        onClick={onNavigate}
                        className={cn(
                          "relative rounded-md px-2.5 py-1.5 text-sm transition-colors",
                          active
                            ? "bg-primary/10 font-medium text-primary"
                            : "text-sidebar-foreground/65 hover:bg-sidebar-accent hover:text-sidebar-foreground"
                        )}
                      >
                        {active && (
                          <span className="absolute inset-y-1.5 start-0 w-0.5 rounded-full bg-primary" />
                        )}
                        {item.title}
                      </Link>
                    );
                  })}
                </div>
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        );
      })}
    </nav>
  );
}
