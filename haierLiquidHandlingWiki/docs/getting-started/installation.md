# Installation Guide

Complete installation instructions for the Haier Liquid Handling System.

## System Requirements

### Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | Intel i5 4th gen | Intel i7 8th gen or newer |
| RAM | 8 GB | 16 GB or more |
| Storage | 50 GB free space | 100 GB SSD |
| USB Ports | 2 USB 3.0 | 4 USB 3.0 |

### Software Requirements

- **Operating System**: Windows 10 (64-bit) or newer
- **Framework**: .NET 6.0 or newer
- **Database**: SQL Server 2019 or newer (Express edition supported)
- **Network**: Ethernet connection recommended

### Supported Hardware

- Haier Liquid Handler Model LH-2000 series
- Haier Liquid Handler Model LH-3000 series
- Compatible third-party devices (see compatibility matrix)

## Installation Steps

### 1. Pre-installation

1. Ensure all hardware requirements are met
2. Close all running applications
3. Disable antivirus temporarily (if required)
4. Ensure you have administrator privileges

### 2. Download

Download the installer from:
- Official website: [Add URL]
- Internal repository: [Add URL]
- Latest release: [Add GitHub/GitLab URL]

### 3. Installation Process

1. **Run the installer**
   ```
   Right-click installer → "Run as administrator"
   ```

2. **Follow the setup wizard**
   - Accept license agreement
   - Choose installation directory
   - Select components to install
   - Configure database connection

3. **Component Selection**
   - [ ] Core Application (Required)
   - [ ] Protocol Designer
   - [ ] Data Analysis Tools
   - [ ] API Server
   - [ ] Documentation

### 4. Database Setup

Choose one of the following options:

#### Option A: Use SQL Server Express (Recommended for single user)
```sql
-- The installer will create the database automatically
Database: HaierLiquidHandling
Instance: .\SQLEXPRESS
```

#### Option B: Use existing SQL Server
```sql
-- Configure connection string
Server: [Your SQL Server]
Database: HaierLiquidHandling
Authentication: Windows/SQL Server
```

### 5. Device Configuration

1. Connect your liquid handling device via USB
2. Install device drivers (included in installer)
3. Run device detection wizard
4. Calibrate the system

## Post-installation

### 1. Verification

Run the system verification tool:
```bash
HaierLH.exe --verify-installation
```

### 2. Initial Setup

1. Launch the application
2. Complete the first-run wizard
3. Create administrator account
4. Configure system settings

### 3. License Activation

1. Open License Manager
2. Enter your license key
3. Activate online or offline
4. Verify activation status

## Troubleshooting Installation Issues

### Common Issues

| Issue | Solution |
|-------|----------|
| Installer won't run | Run as administrator, check antivirus |
| Database connection fails | Verify SQL Server is running, check connection string |
| Device not detected | Check USB connections, install drivers |
| License activation fails | Check internet connection, contact support |

### Log Files

Installation logs are located at:
```
%TEMP%\HaierLiquidHandling\install.log
%APPDATA%\HaierLiquidHandling\logs\
```

## Uninstallation

To remove the software:

1. Use Windows "Add or Remove Programs"
2. Select "Haier Liquid Handling System"
3. Follow uninstall wizard
4. Manually remove data files if needed

## Next Steps

After successful installation:
- Read the [Configuration Guide](configuration.md)
- Follow the [Quick Start Guide](quick-start.md)
- Review the [User Manual](../user-guides/user-manual.md)

---

*Last updated: October 4, 2025*