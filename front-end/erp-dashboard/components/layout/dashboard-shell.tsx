"use client";

import { SidebarProvider, useSidebar } from "@/components/layout/sidebar-provider";
import { CommandMenuProvider, CommandMenu } from "@/components/layout/command-menu";
import { Sidebar } from "@/components/layout/sidebar";
import { Header } from "@/components/layout/header";
import { cn } from "@/lib/utils";

function ShellBody({ children }: { children: React.ReactNode }) {
  const { collapsed } = useSidebar();

  return (
    <div className="min-h-screen">
      <Sidebar />
      <div
        className={cn(
          "flex min-h-screen flex-col transition-[margin] duration-200 ease-in-out",
          collapsed ? "lg:ms-[72px]" : "lg:ms-64"
        )}
      >
        <Header />
        <main className="flex-1 px-4 py-6 md:px-6 lg:px-8">
          <div className="mx-auto w-full max-w-[1600px]">{children}</div>
        </main>
      </div>
      <CommandMenu />
    </div>
  );
}

export function DashboardShell({ children }: { children: React.ReactNode }) {
  return (
    <SidebarProvider>
      <CommandMenuProvider>
        <ShellBody>{children}</ShellBody>
      </CommandMenuProvider>
    </SidebarProvider>
  );
}
