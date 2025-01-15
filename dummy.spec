Name      : dummy-packages
Summary   : Dummy packages to take the place of real packages if they don't exist
Version   : 0.0.%{?build_number}%{!?build_number:x}
Release   : 1
BuildArch : noarch
Packager  : PoiXson <support@poixson.com>
License   : AGPLv3
URL       : https://poixson.com/

Requires  : bash, wget, curl, rsync, grep
Requires  : zip, unzip, tar, gzip

%define _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
%global source_date_epoch_from_changelog 0
%define source_date_epoch 0



%package -n htop-dummy
Summary  : Dummy package for htop
Provides : htop

%package -n nmon-dummy
Summary  : Dummy package for nmon
Provides : nmon

%package -n iotop-c-dummy
Summary  : Dummy package for iotop-c
Provides : iotop-c

%package -n calc-dummy
Summary  : Dummy package for calc
Provides : calc



%description
Dummy packages to take the place of real packages if they don't exist

%description -n htop-dummy
Dummy package for htop

%description -n nmon-dummy
Dummy package for nmon

%description -n iotop-c-dummy
Dummy package for iotop-c

%description -n calc-dummy
Dummy package for calc



%files -n htop-dummy

%files -n nmon-dummy

%files -n iotop-c-dummy

%files -n calc-dummy
