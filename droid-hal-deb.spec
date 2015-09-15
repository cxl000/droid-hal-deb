# These and other macros are documented in dhd/droid-hal-device.inc
%define device deb
%define vendor asus
%define vendor_pretty Asus
%define device_pretty Nexus 7 (2013)
%define installable_zip 1
%define android_config \
#define QCOM_BSP 1\
%{nil}
%include rpm/dhd/droid-hal-device.inc
