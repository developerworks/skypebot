/**
 * 下拉菜单
 * 
 * @author joe.he <developerworks@163.com>
 * @copyright irgs.cn
 */
(function(jQuery) {
	
	jQuery.fn.dropdown = function(settings) {
		var self = this;
		// 默认设置
		if (settings)
			jQuery.extend(jQuery.fn.dropdown.defaults, settings);
		
		// 返回jQuery对象用户链式调用
		return this;
	};
	
	
	/**
	 * 默认配置
	 */
	jQuery.fn.dropdown.defaults = {
		shadowWidth: 5,
		css: {
			outer: 'widget_dropdown_outer',
			shadow: 'widget_dropdown_shadow'
		}
	};
	
	
})(jQuery);