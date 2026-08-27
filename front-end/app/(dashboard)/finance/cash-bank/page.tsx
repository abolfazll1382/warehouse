import { PageHeader } from "@/components/shared/page-header"
import { CashBankAccounts } from "@/components/finance/cash-bank-accounts"
import { cashBankAccounts } from "@/lib/data/finance"

export default function CashBankPage() {
  return (
    <>
      <PageHeader title="صندوق و بانک" description="مانده حساب‌های نقدی و بانکی سازمان" />
      <CashBankAccounts accounts={cashBankAccounts} />
    </>
  )
}
