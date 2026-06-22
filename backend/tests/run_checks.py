from system_scanner import (
    get_battery_health_info,
    get_startup_insights,
    get_suspicious_processes,
    get_thermal_status,
    get_system_info,
    get_large_files,
)

failed = []

print('Running quick runtime checks...')

batt = get_battery_health_info()
print('battery.available ->', batt.get('available'))
if 'available' not in batt:
    failed.append('battery_missing_available')

startup = get_startup_insights()
print('startup.count ->', startup.get('count'))
if 'summary' not in startup:
    failed.append('startup_summary_missing')

susp = get_suspicious_processes(limit=3)
print('suspicious.processes count ->', len(susp.get('processes', [])))
if 'processes' not in susp:
    failed.append('suspicious_missing')

therm = get_thermal_status()
print('thermal.available ->', therm.get('available'))
if 'available' not in therm:
    failed.append('thermal_missing')

sysinfo = get_system_info()
print('system.summary ->', sysinfo.get('summary'))
if 'summary' not in sysinfo:
    failed.append('system_missing')

large = get_large_files()
print('large.files length ->', len(large.get('files', [])))
if 'files' not in large:
    failed.append('large_missing')

if failed:
    print('\nFAILED checks:', failed)
    raise SystemExit(1)

print('\nAll checks passed (basic smoke tests).')
