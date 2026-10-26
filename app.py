import streamlit as st
import math

st.set_page_config(page_title="Layered Biomechanical Failure Matrix", layout="centered")
st.title("🛡️ Advanced Taillight vs. Arm Material Failure Matrix")
st.write("An interactive physics application mapping variable impact durations directly to layered human tissue and polymer failure mechanics.")

# Sidebar Master Configuration
st.sidebar.header("🕹️ Master Impact Variables")
veh_speed_mph = st.sidebar.slider("SUV Reverse Speed (MPH)", 0, 60, 25)
impact_duration_ms = st.sidebar.slider("Impact Duration (Milliseconds)", 5, 30, 15)
temperature_f = st.sidebar.slider("Ambient Temperature (°F)", -40, 120, 70)
impact_angle = st.sidebar.slider("Glancing Impact Angle (Degrees)", 15, 90, 90)

st.sidebar.header("🧍 Pedestrian Variables")
ped_weight_lbs = st.sidebar.slider("Total Pedestrian Weight (Lbs)", 100, 350, 220)
arm_weight_lbs = st.sidebar.slider("Isolated Arm Weight (Lbs)", 5, 20, 11)

# Physics Engine Calculus
speed_fps = veh_speed_mph * 1.46667
impact_duration_sec = impact_duration_ms / 1000.0 

# Coupled Inertial Body Matrix
effective_coupled_mass_lbs = arm_weight_lbs + (0.35 * (ped_weight_lbs - arm_weight_lbs))
coupled_mass_slugs = effective_coupled_mass_lbs / 32.2

# Force Computations
total_potential_force = (coupled_mass_slugs * speed_fps) / impact_duration_sec
direct_peak_force = total_potential_force * math.sin(math.radians(impact_angle))

# Kinematics Readout
shunt_speed_mph = veh_speed_mph * math.cos(math.radians(impact_angle)) + (veh_speed_mph * 0.4) if veh_speed_mph > 0 else 0
rotational_speed_deg_sec = (direct_peak_force * 0.75) / (ped_weight_lbs / 10) if ped_weight_lbs > 0 else 0

# Adjust Polycarbonate Limits
if temperature_f <= 14: shatter_threshold_lbf = 1200
elif temperature_f >= 100: shatter_threshold_lbf = 5000
else: shatter_threshold_lbf = 3500

# Layout Outputs
st.header(f"📊 Live Physics Metrics ({int(direct_peak_force)} lbs of Peak Force)")
c1, c2, c3 = st.columns(3)
with c1: st.metric("Peak Force Transferred", f"{int(direct_peak_force)} lbs")
with c2: st.metric("Body Launch Velocity", f"{round(shunt_speed_mph, 1)} MPH")
with c3: st.metric("Body Spin Speed", f"{int(rotational_speed_deg_sec)} °/s")

# Co-Related Core Analysis
st.header("🔄 Co-Related Material Damage Status")
col_arm, col_lens = st.columns(2)

with col_arm:
    st.markdown("### 🦴 Layered Human Arm Condition")
    if direct_peak_force == 0:
        st.success("No impact.")
    elif direct_peak_force < 100:
        st.success("🟢 **MILD TRAUMA**\n*   **Skin:** Reddening\n*   **Tissue/Muscle:** Capillary bruising\n*   **Bone:** Fully Intact")
    elif direct_peak_force < 300:
        st.info("🟡 **MODERATE TRAUMA**\n*   **Skin:** Deep contusion\n*   **Tissue/Muscle:** Muscle fiber tear & deep swelling\n*   **Bone:** Periosteum bruising; no break")
    elif direct_peak_force < 1200:
        st.warning("🟠 **SEVERE TRAUMA**\n*   **Skin:** Friction avulsions/lacerations\n*   **Tissue/Muscle:** Structural muscle tearing\n*   **Bone:** Structural Failure (Radius/ulna snap)")
    else:
        st.error("💀 **CATASTROPHIC TRAUMA**\n*   **Skin:** Full-thickness skin bursting\n*   **Tissue/Muscle:** Muscle pulpification & vascular shearing\n*   **Bone:** Comminuted Fracture (Pulverized bones)")

with col_lens:
    st.markdown("### 🚨 Lexus Taillight Condition")
    if direct_peak_force == 0: st.success("Vehicle stationary.")
    elif direct_peak_force < shatter_threshold_lbf: st.success(f"✅ **INTACT:** Lens flexes but holds. Below the {int(shatter_threshold_lbf)} lbs shatter limit at {temperature_f}°F.")
    else: st.error(f"💥 **SHATTERED:** Lens structurally fractured into shards. The arm was crushed enough to act as an unyielding solid barrier.")

# Dual-Sided Visual Force Analogies
st.header("💡 Twin Material Force Analogies")
st.write(f"The **{int(direct_peak_force)} lbs** of localized peak impact force is visually equivalent to:")
col_an1, col_an2 = st.columns(2)

with col_an1:
    st.markdown("#### **On the Human Arm:**")
    if direct_peak_force < 300: st.write("• Tripping on a sidewalk and bracing your fall with your arm.")
    elif direct_peak_force < 1200: st.write("• Tucking your bent arm and **jumping out of a 1-story window**, landing directly on your elbow on solid concrete.")
    else: st.write("• Laying your forearm flat on an industrial anvil and having an automated heavy forging press stamp directly down onto the bone.")

with col_an2:
    st.markdown("#### **On the Taillight Housing:**")
    if direct_peak_force < 1200: st.write("• A stray basketball being thrown full-force directly at the plastic lens assembly.")
    elif direct_peak_force < shatter_threshold_lbf: st.write("• Taking a heavy **steel carpenter's framing hammer** and swinging it full-force directly into the center of the lens.")
    else: st.write("• Backing the SUV up and **clipping the sharp edge of a solid brick retaining wall** perfectly on the taillight housing.")
