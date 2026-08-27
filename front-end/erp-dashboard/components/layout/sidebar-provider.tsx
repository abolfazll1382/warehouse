"use client";

import * as React from "react";
import { usePathname } from "next/navigation";
import { navConfig } from "@/lib/nav-config";

function matchGroupForPath(pathname: string): string | null {
  const group = navConfig.find(
    (g) => g.href === pathname || g.items?.some((i) => i.href === pathname)
  );
  return group?.items ? group.id : null;
}

interface SidebarContextValue {
  /** Desktop icon-rail collapse state. */
  collapsed: boolean;
  setCollapsed: (value: boolean) => void;
  toggleCollapsed: () => void;
  /** Mobile off-canvas sheet state. */
  mobileOpen: boolean;
  setMobileOpen: (value: boolean) => void;
  /** Which accordion group is currently expanded (single-open accordion). */
  openGroupId: string | null;
  setOpenGroupId: (id: string | null) => void;
  /** Opens a group and guarantees the sidebar is expanded (used by collapsed icon-rail clicks). */
  openGroupAndExpand: (id: string) => void;
}

const SidebarContext = React.createContext<SidebarContextValue | null>(null);

export function SidebarProvider({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const [collapsed, setCollapsed] = React.useState(false);
  const [mobileOpen, setMobileOpen] = React.useState(false);
  const [openGroupId, setOpenGroupId] = React.useState<string | null>(() =>
    matchGroupForPath(pathname)
  );

  // Keep the expanded accordion group in sync with client-side navigation.
  React.useEffect(() => {
    const matched = matchGroupForPath(pathname);
    if (matched) setOpenGroupId(matched);
    setMobileOpen(false);
  }, [pathname]);

  const toggleCollapsed = React.useCallback(() => setCollapsed((v) => !v), []);

  const openGroupAndExpand = React.useCallback((id: string) => {
    setCollapsed(false);
    setOpenGroupId(id);
  }, []);

  const value = React.useMemo(
    () => ({
      collapsed,
      setCollapsed,
      toggleCollapsed,
      mobileOpen,
      setMobileOpen,
      openGroupId,
      setOpenGroupId,
      openGroupAndExpand,
    }),
    [collapsed, mobileOpen, openGroupId, toggleCollapsed, openGroupAndExpand]
  );

  return <SidebarContext.Provider value={value}>{children}</SidebarContext.Provider>;
}

export function useSidebar() {
  const ctx = React.useContext(SidebarContext);
  if (!ctx) throw new Error("useSidebar must be used within a SidebarProvider");
  return ctx;
}
