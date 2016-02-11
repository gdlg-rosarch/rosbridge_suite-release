Name:           ros-jade-rosbridge-suite
Version:        0.7.14
Release:        0%{?dist}
Summary:        ROS rosbridge_suite package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosbridge_suite
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-rosapi
Requires:       ros-jade-rosbridge-library
Requires:       ros-jade-rosbridge-server
BuildRequires:  ros-jade-catkin

%description
Rosbridge provides a JSON API to ROS functionality for non-ROS programs. There
are a variety of front ends that interface with rosbridge, including a WebSocket
server for web browsers to interact with. Rosbridge_suite is a meta-package
containing rosbridge, various front end packages for rosbridge like a WebSocket
package, and helper packages.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Feb 11 2016 Russell Toris <rctoris@wpi.edu> - 0.7.14-0
- Autogenerated by Bloom

* Fri Aug 14 2015 Russell Toris <rctoris@wpi.edu> - 0.7.13-0
- Autogenerated by Bloom

* Tue Apr 07 2015 Russell Toris <rctoris@wpi.edu> - 0.7.12-0
- Autogenerated by Bloom

