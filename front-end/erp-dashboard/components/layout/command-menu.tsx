"use client";

import * as React from "react";
import { useRouter } from "next/navigation";
import { LayoutDashboard } from "lucide-react";
import { flatNavItems } from "@/lib/nav-config";
import {
  CommandDialog,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
  CommandSeparator,
} from "@/components/ui/command";

interface CommandMenuContextValue {
  open: boolean;
  setOpen: (open: boolean) => void;
}

const CommandMenuContext = React.createContext<CommandMenuContextValue | null>(null);

export function CommandMenuProvider({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = React.useState(false);

  React.useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        setOpen((v) => !v);
      }
    }
    document.addEventListener("keydown", onKeyDown);
    return () => document.removeEventListener("keydown", onKeyDown);
  }, []);

  return (
    <CommandMenuContext.Provider value={{ open, setOpen }}>
      {children}
    </CommandMenuContext.Provider>
  );
}

export function useCommandMenu() {
  const ctx = React.useContext(CommandMenuContext);
  if (!ctx) throw new Error("useCommandMenu must be used within a CommandMenuProvider");
  return ctx;
}

// Group flattened nav items by their parent module for the palette listing.
function groupedNavItems() {
  const map = new Map<string, typeof flatNavItems>();
  for (const item of flatNavItems) {
    const list = map.get(item.groupTitle) ?? [];
    list.push(item);
    map.set(item.groupTitle, list);
  }
  return Array.from(map.entries());
}

export function CommandMenu() {
  const { open, setOpen } = useCommandMenu();
  const router = useRouter();
  const groups = React.useMemo(groupedNavItems, []);

  const go = (href: string) => {
    setOpen(false);
    router.push(href);
  };

  return (
    <CommandDialog open={open} onOpenChange={setOpen}>
      <CommandInput placeholder="جستجو در ماژول‌ها، صفحات و عملیات سامانه..." />
      <CommandList>
        <CommandEmpty>نتیجه‌ای یافت نشد.</CommandEmpty>
        <CommandGroup heading="پرکاربرد">
          <CommandItem value="داشبورد نمای کلی" onSelect={() => go("/")}>
            <LayoutDashboard />
            داشبورد / نمای کلی
          </CommandItem>
        </CommandGroup>
        <CommandSeparator />
        {groups.map(([groupTitle, items]) => (
          <CommandGroup key={groupTitle} heading={groupTitle}>
            {items.map((item) => {
              const Icon = item.icon;
              return (
                <CommandItem
                  key={item.href}
                  value={`${groupTitle} ${item.title}`}
                  onSelect={() => go(item.href)}
                >
                  <Icon />
                  {item.title}
                </CommandItem>
              );
            })}
          </CommandGroup>
        ))}
      </CommandList>
    </CommandDialog>
  );
}
