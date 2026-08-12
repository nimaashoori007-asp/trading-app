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
FONT_CHECK = ("Segoe UI", 10, "bold")


# =========================================================
# برنامه اصلی
# =========================================================

class TradingApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Trading Analysis")
        self.root.geometry("750x800")
        self.root.minsize(650, 650)
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
        # دکمه ریست - بالا سمت راست
        # =================================================

        reset_button = tk.Button(
            frame,
            text="🔄 ریست",
            command=lambda: reset(),
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
            anchor="e",
            padx=25,
            pady=(10, 0)
        )


        # =================================================
        # عنوان بازار
        # =================================================

        tk.Label(
            frame,
            text=market_name,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=FONT_TITLE
        ).pack(
            anchor="w",
            padx=25,
            pady=(10, 10)
        )


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
        # متغیرهای جدا برای هر مرحله
        # =================================================

        stage1_vars = {}
        stage2_vars = {}
        stage3_vars = {}
        stage4_vars = {}


        # =================================================
        # ساخت چک‌باکس
        # =================================================

        def make_checkbox(parent, text, variables):

            var = tk.BooleanVar(value=False)

            checkbox = tk.Checkbutton(
                parent,
                text=text,
                variable=var,
                bg=BG_COLOR,
                activebackground=BG_COLOR,
                fg=TEXT_COLOR,
                activeforeground=TEXT_COLOR,
                font=FONT_CHECK,
                selectcolor="white",
                anchor="w"
            )

            variables[text] = var

            return checkbox


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
            padx=20
        )


        make_checkbox(
            stage1_options,
            "هانت",
            stage1_vars
        ).pack(
            side="left",
            padx=(0, 20)
        )


        make_checkbox(
            stage1_options,
            "ادامه دار",
            stage1_vars
        ).pack(
            side="left",
            padx=(0, 20)
        )


        make_checkbox(
            stage1_options,
            "هیچکدام",
            stage1_vars
        ).pack(
            side="left"
        )


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
            padx=20
        )


        make_checkbox(
            stage2_options,
            "هانت",
            stage2_vars
        ).pack(
            side="left",
            padx=(0, 20)
        )


        make_checkbox(
            stage2_options,
            "BOS",
            stage2_vars
        ).pack(
            side="left",
            padx=(0, 20)
        )


        make_checkbox(
            stage2_options,
            "نقدینگی",
            stage2_vars
        ).pack(
            side="left",
            padx=(0, 20)
        )


        make_checkbox(
            stage2_options,
            "SMT",
            stage2_vars
        ).pack(
            side="left"
        )


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
            padx=20
        )


        make_checkbox(
            stage3_options,
            "Sdp",
            stage3_vars
        ).pack(
            side="left",
            padx=(0, 15)
        )


        make_checkbox(
            stage3_options,
            "هانت لگ",
            stage3_vars
        ).pack(
            side="left",
            padx=(0, 15)
        )


        make_checkbox(
            stage3_options,
            "BOS",
            stage3_vars
        ).pack(
            side="left",
            padx=(0, 15)
        )


        make_checkbox(
            stage3_options,
            "OB",
            stage3_vars
        ).pack(
            side="left",
            padx=(0, 15)
        )


        make_checkbox(
            stage3_options,
            "FVG",
            stage3_vars
        ).pack(
            side="left",
            padx=(0, 15)
        )


        make_checkbox(
            stage3_options,
            "IFVG",
            stage3_vars
        ).pack(
            side="left"
        )


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
            padx=20
        )


        make_checkbox(
            stage4_options,
            "MSS",
            stage4_vars
        ).pack(
            side="left",
            padx=(0, 25)
        )


        make_checkbox(
            stage4_options,
            "CISD",
            stage4_vars
        ).pack(
            side="left",
            padx=(0, 25)
        )


        make_checkbox(
            stage4_options,
            "IFVG",
            stage4_vars
        ).pack(
            side="left"
        )


        # =================================================
        # بررسی مرحله دوم
        # =================================================

        def check_stage2():

            if any(var.get() for var in stage1_vars.values()):

                if not stage2.winfo_ismapped():

                    stage2.pack(
                        anchor="w",
                        fill="x",
                        pady=(15, 0)
                    )

            else:

                stage2.pack_forget()
                stage3.pack_forget()
                stage4.pack_forget()

                for var in stage2_vars.values():
                    var.set(False)

                for var in stage3_vars.values():
                    var.set(False)

                for var in stage4_vars.values():
                    var.set(False)


        # =================================================
        # بررسی مرحله سوم
        # =================================================

        def check_stage3():

            if any(var.get() for var in stage2_vars.values()):

                if not stage3.winfo_ismapped():

                    stage3.pack(
                        anchor="w",
                        fill="x",
                        pady=(15, 0)
                    )

            else:

                stage3.pack_forget()
                stage4.pack_forget()

                for var in stage3_vars.values():
                    var.set(False)

                for var in stage4_vars.values():
                    var.set(False)


        # =================================================
        # بررسی مرحله چهارم
        # =================================================

        def check_stage4():

            if any(var.get() for var in stage3_vars.values()):

                if not stage4.winfo_ismapped():

                    stage4.pack(
                        anchor="w",
                        fill="x",
                        pady=(15, 0)
                    )

            else:

                stage4.pack_forget()

                for var in stage4_vars.values():
                    var.set(False)


        # =================================================
        # ریست
        # =================================================

        def reset():

            for variables in (
                stage1_vars,
                stage2_vars,
                stage3_vars,
                stage4_vars
            ):

                for var in variables.values():
                    var.set(False)

            stage2.pack_forget()
            stage3.pack_forget()
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
        # مخفی بودن مراحل بعدی در شروع
        # =================================================

        stage2.pack_forget()
        stage3.pack_forget()
        stage4.pack_forget()


        # =================================================
        # شروع برنامه
        # =================================================

        update()


# =========================================================
# اجرای برنامه
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = TradingApp(root)

    root.mainloop()
