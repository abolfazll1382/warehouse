import { Landmark, Wallet } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"
import { formatToman } from "@/lib/utils"
import type { CashBankAccount } from "@/lib/data/finance"

export function CashBankAccounts({ accounts }: { accounts: CashBankAccount[] }) {
  const total = accounts.reduce((sum, a) => sum + a.balance, 0)

  return (
    <div className="flex flex-col gap-4">
      <Card className="border-primary/30 bg-gradient-to-l from-primary/10 via-card to-card">
        <CardContent className="flex flex-col gap-1 px-5">
          <p className="text-sm text-muted-foreground">مجموع موجودی نقد و بانک</p>
          <p className="text-3xl font-bold tabular-nums text-foreground">{formatToman(total)}</p>
        </CardContent>
      </Card>

      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-3">
        {accounts.map((account) => {
          const Icon = account.accountType === "صندوق نقدی" ? Wallet : Landmark
          return (
            <Card key={account.id}>
              <CardContent className="flex flex-col gap-4 px-5">
                <div className="flex items-center justify-between">
                  <span className="flex size-10 items-center justify-center rounded-xl bg-primary/10 text-primary">
                    <Icon className="size-5" />
                  </span>
                  <span className="rounded-full bg-secondary px-2.5 py-1 text-xs text-secondary-foreground">
                    {account.accountType}
                  </span>
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">{account.accountName}</p>
                  <p className="mt-1 text-xl font-bold tabular-nums text-foreground">
                    {formatToman(account.balance)}
                  </p>
                </div>
                <p className="text-xs text-muted-foreground tabular-nums">
                  آخرین تراکنش: {account.lastActivity}
                </p>
              </CardContent>
            </Card>
          )
        })}
      </div>
    </div>
  )
}
