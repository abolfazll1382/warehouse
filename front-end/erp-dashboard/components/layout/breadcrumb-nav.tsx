"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { findBreadcrumb } from "@/lib/nav-config";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";

export function BreadcrumbNav() {
  const pathname = usePathname();
  const match = findBreadcrumb(pathname);

  return (
    <Breadcrumb className="hidden md:block">
      <BreadcrumbList>
        <BreadcrumbItem>
          <BreadcrumbLink asChild>
            <Link href="/">داشبورد</Link>
          </BreadcrumbLink>
        </BreadcrumbItem>

        {match?.item && (
          <>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <span className="text-muted-foreground/70">{match.group.title}</span>
            </BreadcrumbItem>
          </>
        )}

        {match && (
          <>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>{match.item ? match.item.title : match.group.title}</BreadcrumbPage>
            </BreadcrumbItem>
          </>
        )}
      </BreadcrumbList>
    </Breadcrumb>
  );
}
