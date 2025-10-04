# Configuration Guide

Configure your Haier Liquid Handling System for optimal performance.

## Initial Configuration

### System Settings

Access system configuration through:
**Settings** → **System Configuration** → **General**

#### Basic Settings
```yaml
system:
  name: "Haier Liquid Handler"
  location: "Lab Room 101"
  timezone: "UTC+8"
  language: "en-US"
  units: "metric"  # metric or imperial
```

#### Performance Settings
```yaml
performance:
  max_concurrent_protocols: 3
  default_timeout: 300  # seconds
  auto_save_interval: 60  # seconds
  log_level: "INFO"  # DEBUG, INFO, WARN, ERROR
```

### Device Configuration

#### Primary Device Setup

1. **Device Detection**
   ```
   Tools → Device Manager → Auto Detect
   ```

2. **Device Calibration**
   - Volume calibration
   - Speed calibration
   - Position calibration
   - Temperature calibration

3. **Device Parameters**
   ```yaml
   device:
     model: "LH-3000"
     serial_number: "HLH3000-2024-001"
     firmware_version: "2.1.4"
     calibration_date: "2024-10-01"
   ```

#### Multi-Device Setup

For multiple devices:
```yaml
devices:
  primary:
    name: "Main Handler"
    port: "COM3"
    priority: 1
  secondary:
    name: "Backup Handler"
    port: "COM4"
    priority: 2
```

## Protocol Configuration

### Default Protocol Settings

```yaml
protocols:
  default_aspirate_speed: 100  # μL/s
  default_dispense_speed: 150  # μL/s
  default_mixing_cycles: 3
  tip_touch_enabled: true
  air_gap_volume: 5  # μL
```

### Protocol Templates

Create reusable protocol templates:

1. **Standard Pipetting**
   - Single channel operations
   - Multi-channel operations
   - Serial dilutions

2. **Advanced Protocols**
   - PCR setup
   - ELISA protocols
   - Custom workflows

## Database Configuration

### Connection Settings

```yaml
database:
  provider: "SqlServer"
  connection_string: "Server=localhost;Database=HaierLiquidHandling;Trusted_Connection=true;"
  timeout: 30
  pool_size: 10
```

### Backup Configuration

```yaml
backup:
  enabled: true
  schedule: "daily"
  time: "02:00"
  retention_days: 30
  location: "C:\Backups\HaierLH"
```

## Security Configuration

### User Authentication

```yaml
security:
  authentication_mode: "windows"  # windows, local, ldap
  password_policy:
    min_length: 8
    require_uppercase: true
    require_numbers: true
    expiry_days: 90
```

### Access Control

Configure user roles and permissions:

| Role | Permissions |
|------|-------------|
| Administrator | Full system access |
| Operator | Run protocols, view results |
| Analyst | View data, generate reports |
| Guest | Read-only access |

### Audit Configuration

```yaml
audit:
  enabled: true
  log_user_actions: true
  log_system_changes: true
  retention_days: 365
```

## Network Configuration

### API Settings

```yaml
api:
  enabled: true
  port: 8080
  authentication: "jwt"
  cors_enabled: true
  rate_limiting:
    requests_per_minute: 100
```

### Remote Monitoring

```yaml
monitoring:
  enabled: true
  endpoint: "https://monitor.haier.com/api"
  api_key: "[Your API Key]"
  send_interval: 300  # seconds
```

## Data Management

### Storage Configuration

```yaml
data:
  results_storage: "database"  # database, file, both
  file_storage_path: "C:\HaierLH\Data"
  compression_enabled: true
  auto_cleanup_days: 180
```

### Export Settings

```yaml
export:
  default_format: "csv"  # csv, xlsx, json, xml
  include_metadata: true
  timestamp_format: "ISO8601"
```

## Maintenance Configuration

### Scheduled Maintenance

```yaml
maintenance:
  auto_maintenance: true
  daily_checks: "06:00"
  weekly_calibration: "sunday_02:00"
  monthly_deep_clean: "first_sunday_01:00"
```

### Alerts and Notifications

```yaml
alerts:
  email_enabled: true
  smtp_server: "smtp.company.com"
  from_address: "liquidhandler@company.com"
  alert_levels:
    - ERROR
    - WARNING
```

## Configuration Files

### Primary Configuration
- **Location**: `%APPDATA%\HaierLiquidHandling\config.yaml`
- **Format**: YAML
- **Backup**: Automatic backup on changes

### Device Configuration
- **Location**: `%APPDATA%\HaierLiquidHandling\devices.yaml`
- **Format**: YAML

### User Configuration
- **Location**: Database table `UserSettings`
- **Per-user settings**: UI preferences, default values

## Environment-Specific Configuration

### Development Environment
```yaml
environment: "development"
debug_mode: true
verbose_logging: true
mock_devices: true
```

### Production Environment
```yaml
environment: "production"
debug_mode: false
verbose_logging: false
mock_devices: false
performance_monitoring: true
```

## Validation and Testing

### Configuration Validation

Run configuration validation:
```bash
HaierLH.exe --validate-config
```

### Test Configuration

Test your configuration:
```bash
HaierLH.exe --test-config --verbose
```

## Backup and Restore

### Backup Configuration
```bash
# Backup current configuration
HaierLH.exe --backup-config --output="C:\Backup\config_backup.zip"
```

### Restore Configuration
```bash
# Restore from backup
HaierLH.exe --restore-config --input="C:\Backup\config_backup.zip"
```

## Troubleshooting Configuration

### Common Issues

| Issue | Solution |
|-------|----------|
| Configuration not loading | Check file permissions, validate YAML syntax |
| Device not responding | Verify device configuration, check connections |
| Database connection failed | Verify connection string, check SQL Server status |
| Performance issues | Review performance settings, check system resources |

### Configuration Logs

Check configuration logs at:
```
%APPDATA%\HaierLiquidHandling\logs\config.log
```

## Next Steps

After configuration:
- Run the [Quick Start Guide](quick-start.md)
- Review [User Manual](../user-guides/user-manual.md)
- Set up [Monitoring](../operations/monitoring.md)

---

*Last updated: October 4, 2025*