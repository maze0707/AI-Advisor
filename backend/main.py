from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from system_scanner import (
    check_software_requirements,
    get_app_compatibility,
    get_app_issue_explanation,
    get_battery_health_info,
    get_large_files,
    get_performance_explanation,
    get_security_check,
    get_slow_apps,
    get_system_diagnostics,
    get_system_info,
    get_storage_insights,
    get_upgrade_advice,
    get_full_diagnosis,
    get_startup_insights,
    get_suspicious_processes,
    get_thermal_status,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI Advisor backend is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/system-info")
def system_info():
    return get_system_info()


@app.get("/advice")
def advice():
    info = get_system_info()

    return {
        "summary": info["summary"],
        "recommendations": info["recommendations"],
    }


@app.get("/slow-apps")
def slow_apps():
    return get_slow_apps()


@app.get("/upgrade-advice")
def upgrade_advice():
    return get_upgrade_advice()


@app.get("/battery-health")
def battery_health():
    return get_battery_health_info()


@app.get("/system-diagnostics")
def system_diagnostics():
    return get_system_diagnostics()


@app.get("/performance-explanation")
def performance_explanation():
    return get_performance_explanation()


@app.get("/storage-insights")
def storage_insights():
    return get_storage_insights()


@app.get("/diagnose")
def diagnose(
    app_name: str | None = None,
    required_memory_gb: float | None = None,
    required_storage_gb: float | None = None,
):
    return get_full_diagnosis(app_name, required_memory_gb, required_storage_gb)


@app.get("/startup-insights")
def startup_insights():
    return get_startup_insights()


@app.get("/suspicious-processes")
def suspicious_processes(limit: int | None = 10):
    return get_suspicious_processes(limit=limit or 10)


@app.get("/thermal-status")
def thermal_status():
    return get_thermal_status()


@app.get("/app-compatibility")
def app_compatibility(
    app_name: str | None = None,
    required_memory_gb: float | None = None,
    required_storage_gb: float | None = None,
):
    return get_app_compatibility(app_name, required_memory_gb, required_storage_gb)


@app.get("/app-issue-explanation")
def app_issue_explanation(
    app_name: str | None = None,
    required_memory_gb: float | None = None,
    required_storage_gb: float | None = None,
):
    return get_app_issue_explanation(app_name, required_memory_gb, required_storage_gb)


@app.get("/security-check")
def security_check():
    return get_security_check()


@app.get("/large-files")
def large_files():
    return get_large_files()


@app.get("/can-run")
def can_run(required_memory_gb: float | None = None, required_storage_gb: float | None = None):
    return check_software_requirements(required_memory_gb, required_storage_gb)
