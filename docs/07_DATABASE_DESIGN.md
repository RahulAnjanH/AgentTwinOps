# Database Design

---

# Database Architecture

PostgreSQL

Stores

- Users
- Infrastructure
- Services
- Incidents

MongoDB

Stores

- Twin Objects
- Historical Metrics
- Simulations
- Recommendations

Redis

Stores

- Cache
- Sessions
- Live Metrics

---

# Users Table

Fields

user_id

name

email

password

role

created_at

updated_at

---

# Infrastructure Table

Fields

service_id

service_name

service_type

status

host

created_at

---

# Metrics Collection

metric_id

service_id

cpu_usage

memory_usage

disk_usage

network_usage

latency

timestamp

---

# Digital Twin Collection

twin_id

service_id

current_state

predicted_state

health_score

failure_probability

last_sync

---

# Simulation Collection

simulation_id

scenario

input_parameters

results

created_at

---

# Recommendation Collection

recommendation_id

service_id

recommendation_type

priority

description

status

created_at

---

# Incident Table

incident_id

service_id

severity

incident_type

resolution_status

timestamp

---

# Entity Relationships

User

↓

Infrastructure

↓

Metrics

↓

Twin

↓

Prediction

↓

Recommendation

↓

Simulation
