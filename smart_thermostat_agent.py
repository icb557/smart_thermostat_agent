import tkinter as tk
from tkinter import ttk

# Define the rules for the smart thermostat
thermostat_rules = {
    "too_cold": "Action: Increase Heat",
    "too_hot": "Action: Decrease Heat / Turn on AC",
    "no_change": "Action: Maintain current temperature"
}

# Simple-Reactive Agent Class
class SmartThermostatAgent:
    def __init__(self, rules):
        self.rules = rules

    def act(self, perception):
        if perception in self.rules:
            return self.rules[perception]
        else:
            return "Action: No specific rule for this perception."

# --- UI Setup and Logic ---
class ThermostatApp:
    def __init__(self, root, agent):
        self.root = root
        self.agent = agent
        self.root.title("Smart Thermostat Simulator")

        # Styling
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ccc")
        style.configure("TLabel", padding=6)
        style.configure("TEntry", padding=6)

        # Frame for Control Buttons
        button_frame = ttk.Frame(root, padding="10")
        button_frame.pack(fill=tk.X)

        self.too_cold_button = ttk.Button(button_frame, text="Too Cold", command=lambda: self.handle_perception("too_cold"))
        self.too_cold_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.too_hot_button = ttk.Button(button_frame, text="Too Hot", command=lambda: self.handle_perception("too_hot"))
        self.too_hot_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.no_change_button = ttk.Button(button_frame, text="No Change", command=lambda: self.handle_perception("no_change"))
        self.no_change_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Frame for Action Display
        action_frame = ttk.Frame(root, padding="10")
        action_frame.pack(fill=tk.X)

        self.action_label = ttk.Label(action_frame, text="Action: ---", font=("Arial", 12))
        self.action_label.pack(pady=10)

    def handle_perception(self, perception_key):
        # current_temp = self.temp_entry.get() # We can use this if logic needs it
        action = self.agent.act(perception_key)
        self.action_label.config(text=action)

if __name__ == "__main__":
    # Create the agent instance
    thermostat_agent = SmartThermostatAgent(thermostat_rules)

    # Set up the Tkinter UI
    main_window = tk.Tk()
    app = ThermostatApp(main_window, thermostat_agent)
    main_window.mainloop() 