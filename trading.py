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


# =========================================================
# فونت‌ها
# =========================================================

# فونت عنوان مراحل حفظ شده
FONT_SECTION = ("Segoe UI", 12, "bold")

# فونت گزینه‌ها حفظ شده
FONT_CHECK = ("Segoe UI", 10, "bold")

# هدر کوچک‌تر
FONT_MARKET = ("Segoe UI", 13, "bold")
FONT_SMALL = ("Segoe UI", 8)


# =========================================================
# برنامه اصلی
# =========================================================

class TradingApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Trading Analysis")

        # اندازه پنجره
        self.root.geometry("820x900")
        self.root.minsize(750, 800)

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
            padx=12,
            pady=10
        )

        # =================================================
        # ساخت بازارها
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
    # تنظیم Notebook
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
            font=("Segoe UI", 10, "bold"),
            padding=[18, 7],
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
        # متغیرهای مرحله
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
            padx=25,
            pady=(5, 3)
        )


        # -------------------------------------------------
        # عنوان بازار
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
            anchor="w"
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
            padx=25,
            pady=(0, 8)
        )


        # =================================================
        # CONTENT
        #
        # این قسمت در نسخه قبلی جا افتاده بود.
        # =================================================

        content = tk.Frame(
            page,
            bg=BG_COLOR
        )

        content.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 8)
        )


        # =================================================
        # ابزار پاک کردن متغیرها
        # =================================================

        def clear_variables(variables):

            for var in variables.values():
                var.set(False)


        # =================================================
        # کارت‌ها
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
                        pady=(0, 10)
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
                        pady=(0, 10)
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
                        pady=(0, 10)
                    )

            else:

                if stage4 is not None:
                    stage4.pack_forget()

                clear_variables(
                    stage4_vars
                )

                stage4_backtest.set(False)


        # =================================================
        # ساخت Checkbox معمولی
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

                padx=2,
                pady=1,

                cursor="hand2"
            )

            variables[text] = var

            return checkbox


        # =================================================
        # ساخت Checkbox بکتست
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

                padx=9,
                pady=4,

                cursor="hand2"
            )


            checkbox.pack(
                anchor="w"
            )


            return backtest_frame


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


            # =================================================
            # Header کارت
            # =================================================

            card_header = tk.Frame(
                card,
                bg=CARD_COLOR
            )

            card_header.pack(
                fill="x",
                padx=15,
                pady=(9, 6)
            )


            # -------------------------------------------------
            # شماره مرحله
            # -------------------------------------------------

            number_label = tk.Label(
                card_header,

                text=str(number),

                bg=ACCENT_COLOR,
                fg="white",

                font=("Segoe UI", 9, "bold"),

                width=3,

                pady=2
            )

            number_label.pack(
                side="left"
            )


            # -------------------------------------------------
            # عنوان مرحله
            # -------------------------------------------------

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


            # =================================================
            # خط جداکننده
            # =================================================

            tk.Frame(
                card,

                bg=BORDER_COLOR,

                height=1
            ).pack(
                fill="x",

                padx=15
            )


            # =================================================
            # گزینه‌ها
            # =================================================

            options_frame = tk.Frame(
                card,

                bg=CARD_COLOR
            )

            options_frame.pack(
                fill="x",

                padx=17,

                pady=(6, 3)
            )


            for option in options:

                make_checkbox(
                    options_frame,
                    option,
                    variables
                ).pack(
                    side="left",
                    padx=(0, 14)
                )


            # =================================================
            # بخش بکتست
            # =================================================

            backtest = make_backtest(
                card,

                backtest_variable,

                backtest_command
            )

            backtest.pack(
                fill="x",

                padx=17,

                pady=(3, 8)
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

            pady=(0, 10)
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
        # در ابتدا فقط مرحله اول دیده شود
        # =================================================

        stage2.pack_forget()
        stage3.pack_forget()
        stage4.pack_forget()


        # =================================================
        # دکمه ریست
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
        # ساخت دکمه ریست
        # =================================================

        reset_button = tk.Button(
            header,

            text="↻  ریست",

            command=reset,

            bg=ACCENT_COLOR,
            fg="white",

            activebackground=ACCENT_HOVER,
            activeforeground="white",

            font=("Segoe UI", 9, "bold"),

            relief="flat",

            cursor="hand2",

            padx=16,
            pady=5,

            bd=0
        )


        reset_button.pack(
            side="right"
        )


# =========================================================
# اجرای برنامه
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TradingApp(root)

    root.mainloop()
