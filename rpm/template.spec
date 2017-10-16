Name:           ros-lunar-rosapi
Version:        0.8.4
Release:        0%{?dist}
Summary:        ROS rosapi package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosapi
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-rosbridge-library
Requires:       ros-lunar-rosgraph
Requires:       ros-lunar-rosnode
Requires:       ros-lunar-rospy
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-rospy

%description
Provides service calls for getting ros meta-information, like list of topics,
services, params, etc.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Oct 16 2017 Russell Toris <rctoris@wpi.edu> - 0.8.4-0
- Autogenerated by Bloom

* Mon Sep 11 2017 Russell Toris <rctoris@wpi.edu> - 0.8.3-0
- Autogenerated by Bloom

* Wed Aug 30 2017 Russell Toris <rctoris@wpi.edu> - 0.8.1-0
- Autogenerated by Bloom

