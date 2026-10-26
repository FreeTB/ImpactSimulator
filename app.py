import streamlit as st
import math

st.set_page_config(page_title="Advanced Biomechanical Impact Matrix", layout="centered")

st.title("🛡️ Advanced Taillight vs. Arm Material Failure Matrix")
st.write("An interactive physics application mapping variable impact durations directly to layered human tissue and polymer failure mechanics.")

# Master Sliding Controls (Placed at the bottom or main page to replicate layout)
st.subheader("🕹️ Simulation Controls")
veh_speed_mph = st.slider("Impact Speed", 0, 60, 35)
impact_duration_ms = st.slider("Impact Duration", 5, 30, 10)
temperature_f = st.slider("Lens Temperature", -40, 120, 68)
impact_angle = st.slider("Glancing Impact Angle (Degrees)", 15, 90, 90)

# Constants based on previous setups
ped_weight_lbs = 220
arm_weight_lbs = 11

# Advanced Physics Engine Calculations
speed_fps = veh_speed_mph * 1.46667
impact_duration_sec = impact_duration_ms / 1000.0 

# Coupled Inertial Body Matrix
effective_coupled_mass_lbs = arm_weight_lbs + (0.35 * (ped_weight_lbs - arm_weight_lbs))
coupled_mass_slugs = effective_coupled_mass_lbs / 32.2

# Force Computations
total_potential_force = (coupled_mass_slugs * speed_fps) / impact_duration_sec
direct_peak_force = total_potential_force * math.sin(math.radians(impact_angle))

# 220 lbs Kinematics Outputs matching the image layout
shunt_speed_mph = int(veh_speed_mph * math.cos(math.radians(impact_angle)) + (veh_speed_mph * 0.4)) if veh_speed_mph > 0 else 0
rotational_speed_deg_sec = int((direct_peak_force * 0.75) / (ped_weight_lbs / 10)) if ped_weight_lbs > 0 else 0

# Adjust Polycarbonate Limits based on Fahrenheit
if temperature_f <= 14: shatter_threshold_lbf = 1200
elif temperature_f >= 100: shatter_threshold_lbf = 5000
else: shatter_threshold_lbf = 3500

# Live Metrics Headers
st.header(f"📊 Live Physics Metrics ({int(direct_peak_force)} lbs of Peak Force)")

# Co-Related Structural Cards Layout
col_arm, col_lens = st.columns(2)

with col_arm:
    st.markdown("### 🦴 Complete Bone Fracture")
    if direct_peak_force < 300:
        st.write("Displaced clean break of the radius/ulna. Requires immediate surgical fixation or casting.")
    elif direct_peak_force < 1200:
        st.write("Displaced clean break of the radius/ulna. Requires immediate surgical fixation or casting.")
    else:
        st.write("💀 **Catastrophic Structural Crush:** Bones are pulverized into fragments, turning the arm into an unyielding compressed mass.")

with col_lens:
    st.markdown("### 🚨 Fracture")
    if direct_peak_force < shatter_threshold_lbf:
        st.write(f"Lens flexes but holds. Below the {int(shatter_threshold_lbf)} lbs shatter limit at {temperature_f}°F.")
    else:
        st.write("Instantaneous puncture and crack propagation across the lens surface. Casing breaks apart.")

# Analogy & Body Metrics Sections Matching Image Layout
st.markdown("---")
st.markdown(f"### 🥊 Boxing Punch Analogy")
st.write(f"Matches a professional heavyweight boxer's clean cross. Calculated force is equivalent to {max(1, round(direct_peak_force / 900, 1))} synchronized heavyweight strikes.")

st.markdown(f"### 🔨 Anvil Kinetic Analogy")
st.write(f"Matches heavy kinetic tooling or industrial drops. Equivalent to a {int(direct_peak_force / 22.2)} lb steel anvil falling 2.3 feet.")

st.markdown("### 🏃‍♂️ 220 lbs Body Metrics")
st.write(f"**Launch speed:** {shunt_speed_mph} MPH")
st.write(f"**Spin speed:** {rotational_speed_deg_sec}° / s")
