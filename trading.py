import tkinter as tk
from tkinter import ttk


# =========================================================
# تنظیمات ظاهری
# =========================================================

BG_COLOR = "#EAF2F8"
TEXT_COLOR = "#17202A"
ACCENT_COLOR = "#5DADE2"

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_SECTION = ("Segoe UI", 12, "bold")
FONT_CHECK = ("Segoe UI", 11, "bold")


# =========================================================
# برنامه اصلی
# =========================================================

class TradingApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Trading Analysis")
        self.root.geometry("700x800")
        self.root.minsize(600, 650)
        self.root.configure(bg=BG_COLOR)

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
            padding=[20, 8]
        )

        notebook = ttk.Notebook(root)

        notebook.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # چهار بازار
        self.create_market(notebook, "Eur")
        self.create_market(notebook, "Nasdaq")
        self.create_market(notebook, "Gbp")
        self.create_market(notebook, "Gold")


    # =====================================================
    # ساخت بازار
    # =====================================================

    def create_market(self, notebook, market_name):

        frame = tk.Frame(
            notebook,
            bg=BG_COLOR
        )

        notebook.add(
            frame,
            text=market_name
        )


        # =================================================
        # عنوان بازار
        # =================================================

        title = tk.Label(
            frame,
            text=market_name,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT_TITLE
        )

        title.pack(
            anchor="w",
            padx=25,
            pady=(20, 10)
        )


        # =================================================
        # کانتینر
        # =================================================

        container = tk.Frame(
            frame,
            bg=BG_COLOR
        )

        container.pack(
            fill="both",
            expand=True,
            padx=25
        )


        # =================================================
        # متغیرهای چک‌باکس
        # =================================================

        variables = {}


        # =================================================
        # ساخت چک‌باکس
        # =================================================

        def checkbox(parent, name):

            var = tk.BooleanVar(value=False)

            cb = tk.Checkbutton(
                parent,
                text=name,
                variable=var,
                bg=BG_COLOR,
                activebackground=BG_COLOR,
                fg=TEXT_COLOR,
                activeforeground=TEXT_COLOR,
                font=FONT_CHECK,
                anchor="w",
                selectcolor="white"
            )

            variables[name] = var

            return cb


        # =================================================
        # مرحله اول
        # =================================================

        stage1 = tk.Frame(
            container,
            bg=BG_COLOR
        )

        stage1.pack(
            anchor="w",
            fill="x"
        )

        tk.Label(
            stage1,
            text="📊 کندل دیلی",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT_SECTION
        ).pack(anchor="w")


        stage1_options = tk.Frame(
            stage1,
            bg=BG_COLOR
        )

        stage1_options.pack(
            anchor="w",
            padx=30
        )


        daily_hunt = checkbox(
            stage1_options,
            "هانت"
        )

        daily_continue = checkbox(
            stage1_options,
            "ادامه دار"
        )

        daily_none = checkbox(
            stage1_options,
            "هیچکدام"
        )


        daily_hunt.pack(anchor="w")
        daily_continue.pack(anchor="w")
        daily_none.pack(anchor="w")


        # =================================================
        # مرحله دوم
        # =================================================

        stage2 = tk.Frame(
            container,
            bg=BG_COLOR
        )

        tk.Label(
            stage2,
            text="↓ تشخیص جهت لگ (4 ساعته و 1 ساعته)",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT_SECTION
        ).pack(anchor="w")


        stage2_options = tk.Frame(
            stage2,
            bg=BG_COLOR
        )

        stage2_options.pack(
            anchor="w",
            padx=30
        )


        direction_hunt = checkbox(
            stage2_options,
            "هانت"
        )

        direction_bos = checkbox(
            stage2_options,
            "BOS"
        )

        direction_liquidity = checkbox(
            stage2_options,
            "نقدینگی"
        )

        direction_smt = checkbox(
            stage2_options,
            "SMT"
        )


        direction_hunt.pack(anchor="w")
        direction_bos.pack(anchor="w")
        direction_liquidity.pack(anchor="w")
        direction_smt.pack(anchor="w")


        # =================================================
        # مرحله سوم
        # =================================================

        stage3 = tk.Frame(
            container,
            bg=BG_COLOR
        )

        tk.Label(
            stage3,
            text="↓ تایم پایین: یافتن ناحیه",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT_SECTION
        ).pack(anchor="w")


        stage3_options = tk.Frame(
            stage3,
            bg=BG_COLOR
        )

        stage3_options.pack(
            anchor="w",
            padx=30
        )


        sdp = checkbox(
            stage3_options,
            "Sdp"
        )

        leg_hunt = checkbox(
            stage3_options,
            "هانت لگ"
        )

        low_bos = checkbox(
            stage3_options,
            "BOS"
        )

        ob = checkbox(
            stage3_options,
            "OB"
        )

        fvg = checkbox(
            stage3_options,
            "FVG"
        )

        ifvg = checkbox(
            stage3_options,
            "IFVG"
        )


        sdp.pack(anchor="w")
        leg_hunt.pack(anchor="w")
        low_bos.pack(anchor="w")
        ob.pack(anchor="w")
        fvg.pack(anchor="w")
        ifvg.pack(anchor="w")


        # =================================================
        # مرحله چهارم
        # =================================================

        stage4 = tk.Frame(
            container,
            bg=BG_COLOR
        )

        tk.Label(
            stage4,
            text="↓ ورود بر اساس",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT_SECTION
        ).pack(anchor="w")


        stage4_options = tk.Frame(
            stage4,
            bg=BG_COLOR
        )

        stage4_options.pack(
            anchor="w",
            padx=30
        )


        mss = checkbox(
            stage4_options,
            "MSS"
        )

        cisd = checkbox(
            stage4_options,
            "CISD"
        )

        entry_ifvg = checkbox(
            stage4_options,
            "IFVG"
        )


        mss.pack(anchor="w")
        cisd.pack(anchor="w")
        entry_ifvg.pack(anchor="w")


        # =================================================
        # نمایش مرحله دوم
        # =================================================

        def check_stage2():

            if (
                variables["هانت"].get()
                or variables["ادامه دار"].get()
                or variables["هیچکدام"].get()
            ):

                stage2.pack(
                    anchor="w",
                    fill="x",
                    pady=(15, 0)
                )

            else:

                stage2.pack_forget()
                stage3.pack_forget()
                stage4.pack_forget()


        # =================================================
        # نمایش مرحله سوم
        # =================================================

        def check_stage3():

            if (
                variables["هانت"].get()
                or variables["BOS"].get()
                or variables["نقدینگی"].get()
                or variables["SMT"].get()
            ):

                stage3.pack(
                    anchor="w",
                    fill="x",
                    pady=(15, 0)
                )

            else:

                stage3.pack_forget()
                stage4.pack_forget()


        # =================================================
        # نمایش مرحله چهارم
        # =================================================

        def check_stage4():

            if (
                variables["Sdp"].get()
                or variables["هانت لگ"].get()
                or variables["OB"].get()
                or variables["FVG"].get()
                or variables["IFVG"].get()
            ):

                stage4.pack(
                    anchor="w",
                    fill="x",
                    pady=(15, 0)
                )

            else:

                stage4.pack_forget()


        # =================================================
        # آپدیت
        # =================================================

        def update():

            check_stage2()
            check_stage3()
            check_stage4()

            self.root.after(
                100,
                update
            )


        # =================================================
        # ریست
        # =================================================

        def reset():

            for var in variables.values():
                var.set(False)

            stage2.pack_forget()
            stage3.pack_forget()
            stage4.pack_forget()


        # =================================================
        # دکمه ریست
        # =================================================

        reset_button = tk.Button(
            frame,
            text="🔄 ریست",
            command=reset,
            bg=ACCENT_COLOR,
            fg="white",
            activebackground="#3498DB",
            activeforeground="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=8
        )

        reset_button.pack(
            side="bottom",
            pady=20
        )


        # شروع بررسی
        update()


# =========================================================
# اجرای برنامه
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TradingApp(root)

    root.mainloop()
