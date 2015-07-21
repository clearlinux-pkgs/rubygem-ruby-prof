#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ruby-prof
Version  : 0.15.8
Release  : 2
URL      : https://rubygems.org/downloads/ruby-prof-0.15.8.gem
Source0  : https://rubygems.org/downloads/ruby-prof-0.15.8.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: rubygem-ruby-prof-bin
Requires: rubygem-ruby-prof-lib
BuildRequires : ruby
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rake-compiler
BuildRequires : rubygem-rdoc

%description
= ruby-prof
{<img src="https://travis-ci.org/ruby-prof/ruby-prof.png?branch=master" alt="Build Status" />}[https://travis-ci.org/ruby-prof/ruby-prof]

%package bin
Summary: bin components for the rubygem-ruby-prof package.
Group: Binaries

%description bin
bin components for the rubygem-ruby-prof package.


%package lib
Summary: lib components for the rubygem-ruby-prof package.
Group: Libraries

%description lib
lib components for the rubygem-ruby-prof package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ruby-prof-0.15.8
gem spec %{SOURCE0} -l --ruby > rubygem-ruby-prof.gemspec

%build
gem build rubygem-ruby-prof.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ruby-prof-0.15.8.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/ruby-prof-0.15.8 && rake test && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/ruby-prof-0.15.8.gem
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/Object/add_define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/Rack/RubyProf/call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/Rack/RubyProf/cdesc-RubyProf.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/Rack/RubyProf/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/Rack/RubyProf/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/Rack/cdesc-Rack.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/cdesc-AbstractPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/method_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/min_percent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/print_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/print_footer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/print_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/print_thread-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/print_threads-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/setup_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AbstractPrinter/sort_method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/aggregate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/aggregate_without_recursion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/call_infos-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/called-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/cdesc-AggregateCallInfo.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/children-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/children_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/line-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/parent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/self_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/target-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/total_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/AggregateCallInfo/wait_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/call_sequence-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/cdesc-CallInfo.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/children_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/descendent_of-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/detect_recursion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/eliminate%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/find_call-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/inspect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/merge_call_tree-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/non_recursive%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/recalc_recursion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/recursive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/root%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/roots_of-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/stack-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfo/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfoPrinter/cdesc-CallInfoPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfoPrinter/print_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfoPrinter/print_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfoVisitor/cdesc-CallInfoVisitor.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfoVisitor/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfoVisitor/visit-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallInfoVisitor/visit_call_info-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/application-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/arguments-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/base64_image-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/cdesc-CallStackPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/color-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/dump-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/expansion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/graph_link-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/link-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/method_href-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/open_asset-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_commands-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_css-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_footer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_help-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_java_script-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_stack-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/print_title_bar-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/sum-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/threshold-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/title-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallStackPrinter/total_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallTreePrinter/cdesc-CallTreePrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallTreePrinter/convert-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallTreePrinter/file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallTreePrinter/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallTreePrinter/print_thread-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/CallTreePrinter/print_threads-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/cdesc-DotPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/dot_id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/mode_name-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/print_classes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/print_edges-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/print_thread-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/print_threads-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/DotPrinter/puts-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/FlatPrinter/cdesc-FlatPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/FlatPrinter/print_footer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/FlatPrinter/print_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/FlatPrinter/print_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/FlatPrinter/sort_method-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/FlatPrinterWithLineNumbers/cdesc-FlatPrinterWithLineNumbers.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/FlatPrinterWithLineNumbers/print_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphHtmlPrinter/cdesc-GraphHtmlPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphHtmlPrinter/create_link-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphHtmlPrinter/file_link-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphHtmlPrinter/method_href-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphHtmlPrinter/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphHtmlPrinter/setup_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphHtmlPrinter/template-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphPrinter/cdesc-GraphPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphPrinter/print_children-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphPrinter/print_footer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphPrinter/print_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphPrinter/print_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/GraphPrinter/print_parents-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/%3c%3d%3e-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/aggregate_children-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/aggregate_parents-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/called-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/cdesc-MethodInfo.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/children-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/children_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/clear_cached_values_which_depend_on_recursiveness-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/detect_recursion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/eliminate%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/min_depth-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/non_recursive%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/non_recursive-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/parents-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/recalc_recursion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/recursive%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/root%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/self_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/to_s-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/total_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MethodInfo/wait_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MultiPrinter/cdesc-MultiPrinter.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MultiPrinter/flat_profile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MultiPrinter/graph_profile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MultiPrinter/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MultiPrinter/print-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MultiPrinter/stack_profile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/MultiPrinter/tree_profile-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/cdesc-Profile.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/eliminate_methods%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/eliminate_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/pause-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/paused%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/post_process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/profile-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/read_regexps_from_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/resume-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/running%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/stop-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Profile/threads-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/cdesc-ProfileTask.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/clean_output_directory-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/create_output_directory-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/define-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/min_percent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/output_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/output_directory-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/printer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ProfileTask/run_script-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Thread/cdesc-Thread.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Thread/detect_recursion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Thread/recalc_recursion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Thread/top_call_infos-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Thread/top_methods-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/Thread/total_time-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/cdesc-RubyProf.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/cpu_frequency-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/disable_gc_stats_if_needed-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/enable_gc_stats_if_needed-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ensure_not_running%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/ensure_running%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/exclude_threads%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/exclude_threads-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/figure_measure_mode-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_allocations-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_cpu_time-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_gc_runs-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_gc_time-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_memory-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_mode%3d-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_mode-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_mode_requires_gc_stats_enabled%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_mode_string-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_process_time-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/measure_wall_time-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/pause-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/profile-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/resume-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/running%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/start-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/start_script-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/RubyProf/stop-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/ext/ruby_prof/page-Makefile.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/ext/ruby_prof/vc/page-ruby_prof_18_vcxproj.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/ext/ruby_prof/vc/page-ruby_prof_19_vcxproj.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/ext/ruby_prof/vc/page-ruby_prof_20_vcxproj.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/ext/ruby_prof/vc/page-ruby_prof_sln.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/lib/ruby-prof/assets/page-call_stack_printer_css_html.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/lib/ruby-prof/assets/page-call_stack_printer_js_html.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-prof-0.15.8/ri/unknown/cdesc-unknown.ri
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/ruby-prof-0.15.8/gem.build_complete
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/ruby-prof-0.15.8/gem_make.out
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/ruby-prof-0.15.8/mkmf.log
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/CHANGES
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/bin/ruby-prof
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/bin/ruby-prof-check-trace
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/created.rid
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/css/fonts.css
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/css/rdoc.css
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/fonts/Lato-Light.ttf
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/fonts/Lato-LightItalic.ttf
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/fonts/Lato-Regular.ttf
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/fonts/Lato-RegularItalic.ttf
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/fonts/SourceCodePro-Bold.ttf
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/fonts/SourceCodePro-Regular.ttf
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/images/loadingAnimation.gif
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/darkfish.js
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/jquery.js
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/navigation.js
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/navigation.js.gz
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/search.js
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/search_index.js
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/search_index.js.gz
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/searcher.js
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/doc/js/searcher.js.gz
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/flat.txt
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/graph.dot
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/graph.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/graph.txt
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/multi.flat.txt
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/multi.graph.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/multi.grind.dat
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/multi.stack.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples/stack.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples2/graph.dot
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples2/multi.flat.txt
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples2/multi.graph.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples2/multi.grind.dat
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples2/multi.stack.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/examples2/stack.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/Makefile
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/extconf.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_call_info.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_call_info.h
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_call_info.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure.h
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_allocations.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_allocations.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_cpu_time.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_cpu_time.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_gc_runs.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_gc_runs.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_gc_time.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_gc_time.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_memory.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_memory.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_process_time.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_process_time.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_wall_time.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_measure_wall_time.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_method.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_method.h
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_method.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_stack.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_stack.h
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_stack.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_thread.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_thread.h
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/rp_thread.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/ruby_prof.c
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/ruby_prof.h
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/ruby_prof.o
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/vc/ruby_prof.sln
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/vc/ruby_prof_18.vcxproj
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/vc/ruby_prof_19.vcxproj
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/vc/ruby_prof_20.vcxproj
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/aggregate_call_info.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/assets/call_stack_printer.css.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/assets/call_stack_printer.js.html
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/assets/call_stack_printer.png
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/call_info.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/call_info_visitor.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/compatibility.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/method_info.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/abstract_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/call_info_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/call_stack_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/call_tree_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/dot_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/flat_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/flat_printer_with_line_numbers.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/graph_html_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/graph_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/printers/multi_printer.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/profile.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/rack.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/task.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/thread.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby-prof/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/unprof.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ruby-prof.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/aggregate_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/basic_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/block_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/call_info_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/call_info_visitor_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/duplicate_names_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/dynamic_method_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/enumerable_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/exceptions_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/exclude_threads_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/fiber_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/line_number_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/measure_allocations_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/measure_cpu_time_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/measure_gc_runs_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/measure_gc_time_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/measure_memory_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/measure_process_time_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/measure_wall_time_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/method_elimination_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/module_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/multi_printer_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/no_method_class_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/pause_resume_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/prime.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/printers_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/rack_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/recursive_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/singleton_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/stack_printer_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/stack_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/start_stop_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/thread_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/unique_call_path_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/test/yarv_test.rb
/usr/lib64/ruby/gems/2.2.0/specifications/ruby-prof-0.15.8.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/ruby-prof
/usr/bin/ruby-prof-check-trace

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/ruby-prof-0.15.8/ruby_prof.so
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/ext/ruby_prof/ruby_prof.so
/usr/lib64/ruby/gems/2.2.0/gems/ruby-prof-0.15.8/lib/ruby_prof.so
