import React from 'react';
import { Select, Space } from 'antd';

const handleChange = (value: string) => {
  console.log(`selected ${value}`);
};

const DropDown: React.FC = () => (
  <Space wrap>
    <Select
      placeholder="Select a exercise"
      style={{ width: 300}}
      onChange={handleChange}
      options={[
        { value: 'Crunch', label: 'Crunch'},
        { value: 'JumpRope', label: 'Jump rope' },
        { value: 'PushUp', label: 'Push up' },
        { value: 'PullUp', label: 'Pull up' },
        { value: 'Squat', label: 'Squat' },
      ]}
    />
  </Space>
);

export default DropDown;