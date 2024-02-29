from application.commands.add_payment_command import AddPaymentCommand
from application.commands.add_discount_command import AddDiscountCommand
from application.commands.pay_command import PayCommand
from application.commands.undo_payment_command import UndoPaymentCommand
from application.data_store import DataStore


if __name__ == "__main__":
    # Crear una instancia de DataStore
    data_store = DataStore(file_name="payment_details.json")

    # Ejecutar comandos
    payment_cmd = AddPaymentCommand(payment_method="credit", amount=150.0)
    payment_cmd.execute()

    # import pdb; pdb.set_trace()
    add_discount_command = AddDiscountCommand(
        payment=payment_cmd.payment,
        reason="best_client",
        discount_type="amount",
        value=-5.0,
    )
    add_discount_command.execute()

    add_discount_command = AddDiscountCommand(
        payment=payment_cmd.payment,
        reason="client_birthday",
        discount_type="percentage",
        value=5.0,
    )
    add_discount_command.execute()

    pay_command = PayCommand(payment=payment_cmd.payment, data_store=data_store)
    pay_command.execute()

    undo_payment_command = UndoPaymentCommand(data_store=data_store)
    undo_payment_command.execute()
