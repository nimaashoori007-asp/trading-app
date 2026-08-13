import tkinter as tk
from tkinter import ttk


# =========================================================
# تنظیمات ظاهری
# =========================================================

BG_COLOR = "#F4F7FB"
CARD_COLOR = "#FFFFFF"
TEXT_COLOR = "#17202A"
SECONDARY_TEXT = "#5D6D7E"

ACCENT_COLOR = "#3498DB"
ACCENT_HOVER = "#2980B9"

BORDER_COLOR = "#D6E0EA"
BACKTEST_BG = "#F0F8FF"
BACKTEST_BORDER = "#CFE8FA"

FONT_MARKET = ("Segoe UI", 16, "bold")
FONT_SECTION = ("Segoe UI", 12, "bold")
FONT_CHECK = ("Segoe UI", 10, "bold")
FONT_SMALL = ("Segoe UI", 9)


# =========================================================
# برنامه اصلی
# =========================================================

class TradingApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Trading Analysis")

        # پنجره بلندتر تا چهار مرحله بدون اسکرول جا شوند
        self.root.geometry("820x950")
        self.root.minsize(750, 850)

        self.root.configure(
            bg=BG_COLOR
        )

        self.setup_style()

        # =================================================
        # Notebook
        # =================================================

        self.notebook = ttk.Notebook(root)

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=18,
            pady=18
        )

        # =================================================
        # بازارها
        # =================================================

        self.create_market(
            self.notebook,
            "Eur"
        )

        self.create_market(
            self.notebook,
            "Nasdaq"
        )

        self.create_market(
            self.notebook,
            "Gbp"
        )

        self.create_market(
            self.notebook,
            "Gold"
        )


    # =====================================================
    # تنظیمات ttk
    # =====================================================

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "TNotebook",
            background=BG_COLOR,
            borderwidth=0
        )

        style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 11, "bold"),
            padding=[24, 10],
            background="#E8EEF5",
            foreground=TEXT_COLOR
        )

        style.map(
            "TNotebook.Tab",
            background=[
                ("selected", CARD_COLOR)
            ],
            foreground=[
                ("selected", ACCENT_COLOR)
            ]
        )


    # =====================================================
    # ساخت بازار
    # =====================================================

    def create_market(
        self,
        notebook,
        market_name
    ):

        # =================================================
        # صفحه بازار
        # =================================================

        page = tk.Frame(
            notebook,
            bg=BG_COLOR
        )

        notebook.add(
            page,
            text=market_name
        )


        # =================================================
        # متغیرها
        # =================================================

        stage1_vars = {}
        stage2_vars = {}
        stage3_vars = {}
        stage4_vars = {}

        stage1_backtest = tk.BooleanVar(
            value=False
        )

        stage2_backtest = tk.BooleanVar(
            value=False
        )

        stage3_backtest = tk.BooleanVar(
            value=False
        )

        stage4_backtest = tk.BooleanVar(
            value=False
        )


        # =================================================
        # Header
        # =================================================

        header = tk.Frame(
            page,
            bg=BG_COLOR
        )

        header.pack(
            fill="x",
            padx=28,
            pady=(18, 8)
        )


        # -------------------------------------------------
        # عنوان
        # -------------------------------------------------

        title_frame = tk.Frame(
            header,
            bg=BG_COLOR
        )

        title_frame.pack(
            side="left"
        )


        tk.Label(
            title_frame,
            text="TRADING ANALYSIS",
            bg=BG_COLOR,
            fg=SECONDARY_TEXT,
            font=FONT_SMALL
        ).pack(
            anchor="w"
        )


        tk.Label(
            title_frame,
            text=market_name,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT_MARKET
        ).pack(
            anchor="w",
            pady=(1, 0)
        )


        # =================================================
        # دکمه ریست
        # =================================================

        reset_button_frame = tk.Frame(
            header,
            bg=BG_COLOR
        )

        reset_button_frame.pack(
            side="right"
        )


        # =================================================
        # خط جداکننده
        # =================================================

        separator = tk.Frame(
            page,
            bg=BORDER_COLOR,
            height=1
        )

        separator.pack(
            fill="x",
            padx=28,
            pady=(0, 14)
        )


        # =================================================
        # کانتینر مراحل
        # =================================================

        content = tk.Frame(
            page,
            bg=BG_COLOR
        )

        content.pack(
            fill="both",
            expand=True,
            padx=28,
            pady=(0, 10)
        )


        # =================================================
        # ابزار پاک کردن متغیرها
        # =================================================

        def clear_variables(
            variables
        ):

            for var in variables.values():

                var.set(False)


        # =================================================
        # ساخت چک‌باکس
        # =================================================

        def make_checkbox(
            parent,
            text,
            variables
        ):

            var = tk.BooleanVar(
                value=False
            )

            checkbox = tk.Checkbutton(
                parent,
                text=text,
                variable=var,
                bg=CARD_COLOR,
                activebackground=CARD_COLOR,
                fg=TEXT_COLOR,
                activeforeground=TEXT_COLOR,
                font=FONT_CHECK,
                selectcolor="white",
                anchor="w",
                bd=0,
                highlightthickness=0,
                padx=3,
                pady=2,
                cursor="hand2"
            )

            variables[text] = var

            return checkbox


        # =================================================
        # ساخت بکتست
        # =================================================

        def make_backtest(
            parent,
            variable,
            command
        ):

            backtest_frame = tk.Frame(
                parent,
                bg=BACKTEST_BG,
                highlightbackground=BACKTEST_BORDER,
                highlightthickness=1
            )

            checkbox = tk.Checkbutton(
                backtest_frame,
                text="آیا براساس بکتست است؟",
                variable=variable,
                command=command,
                bg=BACKTEST_BG,
                activebackground=BACKTEST_BG,
                fg=ACCENT_COLOR,
                activeforeground=ACCENT_HOVER,
                font=FONT_CHECK,
                selectcolor="white",
                anchor="w",
                bd=0,
                highlightthickness=0,
                padx=10,
                pady=5,
                cursor="hand2"
            )

            checkbox.pack(
                anchor="w"
            )

            return backtest_frame


        # =================================================
        # متغیر کارت‌ها
        # =================================================

        stage1 = None
        stage2 = None
        stage3 = None
        stage4 = None


        # =================================================
        # مرحله دوم
        # =================================================

        def check_stage2():

            if stage1_backtest.get():

                if (
                    stage2 is not None
                    and not stage2.winfo_ismapped()
                ):

                    stage2.pack(
                        fill="x",
                        pady=(0, 14)
                    )

            else:

                if stage2 is not None:
                    stage2.pack_forget()

                if stage3 is not None:
                    stage3.pack_forget()

                if stage4 is not None:
                    stage4.pack_forget()

                clear_variables(
                    stage2_vars
                )

                clear_variables(
                    stage3_vars
                )

                clear_variables(
                    stage4_vars
                )

                stage2_backtest.set(False)
                stage3_backtest.set(False)
                stage4_backtest.set(False)


        # =================================================
        # مرحله سوم
        # =================================================

        def check_stage3():

            if stage2_backtest.get():

                if (
                    stage3 is not None
                    and not stage3.winfo_ismapped()
                ):

                    stage3.pack(
                        fill="x",
                        pady=(0, 14)
                    )

            else:

                if stage3 is not None:
                    stage3.pack_forget()

                if stage4 is not None:
                    stage4.pack_forget()

                clear_variables(
                    stage3_vars
                )

                clear_variables(
                    stage4_vars
                )

                stage3_backtest.set(False)
                stage4_backtest.set(False)


        # =================================================
        # مرحله چهارم
        # =================================================

        def check_stage4():

            if stage3_backtest.get():

                if (
                    stage4 is not None
                    and not stage4.winfo_ismapped()
                ):

                    stage4.pack(
                        fill="x",
                        pady=(0, 14)
                    )

            else:

                if stage4 is not None:
                    stage4.pack_forget()

                clear_variables(
                    stage4_vars
                )

                stage4_backtest.set(False)


        # =================================================
        # ساخت کارت مرحله
        # =================================================

        def create_stage_card(
            parent,
            number,
            title,
            variables,
            options,
            backtest_variable,
            backtest_command
        ):

            card = tk.Frame(
                parent,
                bg=CARD_COLOR,
                highlightbackground=BORDER_COLOR,
                highlightthickness=1
            )


            # -------------------------------------------------
            # Header کارت
            # -------------------------------------------------

            card_header = tk.Frame(
                card,
                bg=CARD_COLOR
            )

            card_header.pack(
                fill="x",
                padx=16,
                pady=(12, 8)
            )


            # شماره

            number_label = tk.Label(
                card_header,
                text=str(number),
                bg=ACCENT_COLOR,
                fg="white",
                font=("Segoe UI", 10, "bold"),
                width=3,
                pady=2
            )

            number_label.pack(
                side="left"
            )


            # عنوان مرحله
            #
            # FONT_SECTION حفظ شده
            #

            tk.Label(
                card_header,
                text=title,
                bg=CARD_COLOR,
                fg=TEXT_COLOR,
                font=FONT_SECTION
            ).pack(
                side="left",
                padx=10
            )


            # -------------------------------------------------
            # خط
            # -------------------------------------------------

            tk.Frame(
                card,
                bg=BORDER_COLOR,
                height=1
            ).pack(
                fill="x",
                padx=16
            )


            # -------------------------------------------------
            # گزینه‌ها
            # -------------------------------------------------

            options_frame = tk.Frame(
                card,
                bg=CARD_COLOR
            )

            options_frame.pack(
                fill="x",
                padx=18,
                pady=(9, 5)
            )


            for option in options:

                make_checkbox(
                    options_frame,
                    option,
                    variables
                ).pack(
                    side="left",
                    padx=(0, 16)
                )


            # -------------------------------------------------
            # بکتست
            # -------------------------------------------------

            backtest = make_backtest(
                card,
                backtest_variable,
                backtest_command
            )

            backtest.pack(
                fill="x",
                padx=18,
                pady=(4, 11)
            )


            return card


        # =================================================
        # مرحله ۱
        # =================================================

        stage1 = create_stage_card(
            content,
            1,
            "📊  کندل دیلی",
            stage1_vars,
            [
                "هانت",
                "ادامه دار",
                "هیچکدام"
            ],
            stage1_backtest,
            check_stage2
        )

        stage1.pack(
            fill="x",
            pady=(0, 14)
        )


        # =================================================
        # مرحله ۲
        # =================================================

        stage2 = create_stage_card(
            content,
            2,
            "تشخیص جهت لگ  (4 ساعته و 1 ساعته)",
            stage2_vars,
            [
                "هانت",
                "BOS",
                "نقدینگی",
                "SMT"
            ],
            stage2_backtest,
            check_stage3
        )


        # =================================================
        # مرحله ۳
        # =================================================

        stage3 = create_stage_card(
            content,
            3,
            "تایم پایین: یافتن ناحیه",
            stage3_vars,
            [
                "Sdp",
                "هانت لگ",
                "BOS",
                "OB",
                "FVG",
                "IFVG"
            ],
            stage3_backtest,
            check_stage4
        )


        # =================================================
        # مرحله ۴
        # =================================================

        stage4 = create_stage_card(
            content,
            4,
            "ورود بر اساس",
            stage4_vars,
            [
                "MSS",
                "CISD",
                "IFVG"
            ],
            stage4_backtest,
            lambda: None
        )


        # =================================================
        # مخفی کردن مراحل بعدی
        # =================================================

        stage2.pack_forget()
        stage3.pack_forget()
        stage4.pack_forget()


        # =================================================
        # ریست
        # =================================================

        def reset():

            clear_variables(
                stage1_vars
            )

            clear_variables(
                stage2_vars
            )

            clear_variables(
                stage3_vars
            )

            clear_variables(
                stage4_vars
            )

            stage1_backtest.set(False)
            stage2_backtest.set(False)
            stage3_backtest.set(False)
            stage4_backtest.set(False)

            stage2.pack_forget()
            stage3.pack_forget()
            stage4.pack_forget()


        # =================================================
        # دکمه ریست
        # =================================================

        reset_button = tk.Button(
            reset_button_frame,
            text="↻  ریست",
            command=reset,
            bg=ACCENT_COLOR,
            fg="white",
            activebackground=ACCENT_HOVER,
            activeforeground="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=7,
            bd=0
        )

        reset_button.pack()


# =========================================================
# اجرای برنامه
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TradingApp(root)

    root.mainloop()
