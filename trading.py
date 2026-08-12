# =================================================
# دکمه ریست - بالا سمت راست
# =================================================

tk.Button(
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
).pack(
    anchor="e",
    padx=25,
    pady=(10, 0)
)
