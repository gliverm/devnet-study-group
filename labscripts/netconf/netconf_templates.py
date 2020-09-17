#!/usr/bin/env python

CREATE_OC_IPV4_ACL = """
<config>
  <acl xmlns="http://openconfig.net/yang/acl">
    <acl-sets>
    {% for acl in acl_sets %}
    <acl-set>
        <name>{{ acl.name }}</name>
        <type>ACL_IPV4</type>
        <config>
          <name>{{ acl.name }}</name>
          <type>ACL_IPV4</type>
        </config>
        <acl-entries>
        {% for entry in acl.entries %}
          <acl-entry>
            <sequence-id>{{ entry.seq }}</sequence-id>
            <config>
              <sequence-id>{{ entry.seq }}</sequence-id>
            </config>
            <ipv4>
              <config>
                <source-address>{{ entry.src }}</source-address>
                <destination-address>{{ entry.dst }}</destination-address>
                <protocol>{{ entry.protocol }}</protocol>
              </config>
            </ipv4>
            {% if acl.src_port is defined %}
            <transport>
              <config>
                <source-port>{{ entry.src_port | d('ANY') }}</source-port>
                <destination-port>{{ entry.dst_port | d('ANY') }}</destination-port>
              </config>
            </transport>
            {% endif %}
            <actions>
              <config>
                <forwarding-action>{{ entry.action }}</forwarding-action>
                <log-action>{{ entry.log_action | d('LOG_NONE') }}</log-action>
              </config>
            </actions>
          </acl-entry>
        {% endfor %}
        </acl-entries>
      </acl-set>
    {% endfor %}
    </acl-sets>
  </acl>
</config>
"""